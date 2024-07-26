from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

def main(request):
    products = Product.objects.all()
    return render(request, 'main/index.html', {'products': products})
