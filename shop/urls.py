from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/<slug:category_slug>', views.home, name='product_by_name'),
    path('products/<slug:category_slug>/<slug:product_slug>',
         views.product, name='product_detail'),
    path('cart', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>', views.add_cart, name='add_cart'),
]