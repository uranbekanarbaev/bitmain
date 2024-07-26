from django.db import models

class Product(models.Model):
    # Basic Information
    img = models.ImageField(upload_to='uploads/', default='uploads/default_JTYzTgS.png')
    name = models.CharField(max_length=100, default='Asic')
    price = models.PositiveIntegerField(null=True, default=0)
    link = models.URLField(max_length=200, default='https://shop.bitmain.com')
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name