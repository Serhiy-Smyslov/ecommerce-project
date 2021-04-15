from django.shortcuts import render, get_object_or_404
from .models import Category, Product


# Create your views here.
def home(request, category_slug=None):
    category_page = None
    products = None
    if category_slug:
        category_page = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.all().filter(category=category_page,
                                                available=True)
    else:
        products = Product.objects.all().filter(available=True)
    return render(request, 'home.html', {
        'products': products,
        'category': category_page,
    })


def product(request):
    return render(request, 'product.html')