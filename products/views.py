from django.shortcuts import render
from .models import Product


def all_products(request):
    """A view to show products"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
