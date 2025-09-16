import uuid
from django.db import models

# Create your models here.

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('BALL', 'Ball'),
        ('BOOT', 'Football Boots'),
        ('KIT', 'Kits & Jerseys'),
        ('EQUI', 'Equipment'),
        ('ACCS', 'Accessories'),
        ('OTHR', 'Other Football Items'),
    ]
    
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.IntegerField(help_text="Price of the product in IDR")
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='OTHR')
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name