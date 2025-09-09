from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'nama': 'Iqbal Rafi Nuryana',
        'class': 'A'
    }
    
    return render(request, "main.html", context)