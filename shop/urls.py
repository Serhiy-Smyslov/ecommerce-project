from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:category_slug>', views.home, name='product_by_name'),
    path('product/', views.product, name='product'),
]