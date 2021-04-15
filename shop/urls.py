from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/<slug:category_slug>',
         views.home, name='product_by_name'),
    path('products/<slug:category_slug>/<slug:product_slug>',
         views.product, name='product_detail'),
    path('cart', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>',
         views.add_cart, name='add_cart'),
    path('cart/remove/<int:product_id>',
         views.cart_remove, name='cart_remove'),
    path('cart/remove_product/<int:product_id>',
         views.cart_remove_product, name='cart_remove_product'),
    path('account/create/', views.sing_up_view, name='sing_up'),
    path('account/login/', views.login_view, name='log_in'),
    path('account/singout/', views.singout_view, name='sing_out'),
]