from django.urls import path
from django.urls.conf import include
from catalog import views

app_name = 'catalog'
urlpatterns = [
    path('category/<int:category_id>', views.category, name='category'),
    path('category/<int:category_id>/product/<int:product_id>', views.product, name='product'),
]