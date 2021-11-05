from django.db import models


class Category(models.Model):
    """
    Modelo de categorias
    """
    name = models.CharField(max_length=144)
    status = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Clase que permite modelar un producto
    """

    name = models.CharField(max_length=144)
    image = models.ImageField(upload_to='catalog/')
    sku = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    short_description = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.BooleanField()
    sort_order = models.PositiveIntegerField(default=0)
    
    categories = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

