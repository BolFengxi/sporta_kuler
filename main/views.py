import json
from django.shortcuts import render, redirect, get_object_or_404
from main.models import Product
from main.forms import ProductsForm
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import requests
from django.utils.html import strip_tags

    
# Create your views here.

@csrf_exempt
def create_product_flutter(request):
    """
    Membuat objek Product baru dari data yang dikirim oleh aplikasi Flutter.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # --- Ambil dan Bersihkan Data ---
            name = strip_tags(data.get("name", "")) 
            description = strip_tags(data.get("description", ""))
            
            # Ambil price, konversi ke integer. Gunakan 0 jika tidak ada atau bukan angka.
            try:
                price = int(data.get("price", 0)) 
            except ValueError:
                price = 0
            
            thumbnail = data.get("thumbnail", "") # URLField, tidak perlu strip_tags
            category = data.get("category", "OTHR") # Gunakan default 'OTHR'
            is_featured = data.get("is_featured", False) # Nilai boolean
            
            # Asumsi pengguna sudah diautentikasi dan tersedia di request.user
            # Jika pengguna diperlukan, pastikan middleware dan autentikasi sudah diatur.
            user = request.user 
            
            # --- Buat dan Simpan Objek Product ---
            new_product = Product(
                user=user,
                name=name, 
                price=price,
                description=description,
                thumbnail=thumbnail,
                category=category,
                is_featured=is_featured,
            )
            new_product.save()
            
            return JsonResponse({"status": "success", "message": "Product successfully created"}, status=201)
        
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON format"}, status=400)
        except Exception as e:
            # Penanganan kesalahan umum
            return JsonResponse({"status": "error", "message": f"An error occurred: {str(e)}"}, status=500)
            
    else:
        return JsonResponse({"status": "error", "message": "Only POST requests are allowed"}, status=405)

def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        # Fetch image from external source
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        # Return the image with proper content type
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')

            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({
                    "success": True,
                    "message": "Account created successfully! Redirecting to login...",
                    "redirect_url": reverse("main:login")
                })
            
            return redirect("main:login")

        else:
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({
                    "success": False,
                    "errors": form.errors,
                    "message": "Please correct the errors below."
                })

    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))

            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    "success": True,
                    "message": "Login successful! Redirecting...",
                    "redirect_url": reverse("main:show_main")
                })

            return response

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({
                "success": False,
                "errors": form.errors,
                "message": "Invalid credentials. Please try again."
            })

    else:
        form = AuthenticationForm(request)

    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter","all")
    if filter_type == "all":
        products_list = Product.objects.all()
    else:
        products_list = Product.objects.filter(user=request.user)
    
    context = {
        'npm' : '2406417462',
        'name': 'Iqbal Rafi Nuryana',
        'class': 'A',
        'products_list': products_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'username': request.user.username,
    }
    return render(request, "main.html", context)

def create_product(request):
    form = ProductsForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()

            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({
                    "success": True,
                    "message": "Product created successfully!",
                    "redirect_url": reverse("main:show_main"),
                })

            return redirect("main:show_main")
        else:
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({
                    "success": False,
                    "errors": form.errors,
                    "message": "Please fix the errors below."
                })

    context = {"form": form}
    return render(request, "create_product.html", context)

def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = ProductsForm(request.POST or None, instance=product)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            # 🔹 Respon JSON kalau AJAX
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({
                    "success": True,
                    "message": "Product updated successfully!",
                    "redirect_url": reverse("main:show_main"),
                })
            
            return redirect('main:show_main')
        else:
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({
                    "success": False,
                    "errors": form.errors,
                    "message": "Please correct the errors below."
                })

    context = {'form': form, 'product': product}
    return render(request, "edit_product.html", context)


def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@login_required(login_url='/login')
def show_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    context = {
        'product': product,
    }
    return render(request, 'product_detail.html', context)

def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")
 
def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'product_id': str(product.product_id),
            'name' : product.name,
            'price' : product.price,
            'description' : product.description,
            'thumbnail' : product.thumbnail,
            'category' : product.category,
            'is_featured' : product.is_featured,
            'user_id' : product.user.id if product.user else None,
        }
        for product in product_list
    ]
    return JsonResponse(data, safe=False)


def show_xml_by_id(request, product_id):
   try:
       product_item = Product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)
   
def show_json_by_id(request, product_id):
   try:
       product = Product.objects.select_related('user').get(pk=product_id)
       data = {
            'id' : str(product.product_id),
            'name' : product.name,
            'price' : product.price,
            'description' : product.description,
            'thumbnail' : product.thumbnail,
            'category' : product.category,
            'is_featured' : product.is_featured,
            'user_id': str(product.user.id) if product.user else None,
            'user_username': product.user.username if product.user else "Anonymous",
       }
       return JsonResponse(data)
   except Product.DoesNotExist:
       return JsonResponse({'detail' : 'Not found'}, status=404)
   
@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = request.POST.get("name")
    description = request.POST.get("description")
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    price = request.POST.get("price")
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    user = request.user
    
    new_product =  Product(
        name = name,
        description = description,
        category = category,
        thumbnail = thumbnail,
        price = price,
        is_featured = is_featured,
        user = user
    )
    new_product.save()
    
    return HttpResponse(b"CREATED", status=201)
