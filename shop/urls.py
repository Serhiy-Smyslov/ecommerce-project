from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:category_slug>', views.home, name='product_by_name'),
    path('<slug:category_slug>/<slug:product_slug>',
         views.product, name='product_detail'),
]