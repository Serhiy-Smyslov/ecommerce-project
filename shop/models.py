from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Save information about category on platform."""
    name = models.CharField(max_length=250, unique=True)
    slug = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="category", blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('product_by_name', args=[self.slug])


class Product(models.Model):
    """Save information about product on platform."""
    name = models.CharField(max_length=250, unique=True)
    slug = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    # Connect objects from class Category
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="product", blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug,
                                               self.slug])
