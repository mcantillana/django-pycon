from django.core.paginator import (
    Paginator, 
    EmptyPage, 
    PageNotAnInteger
)
from django.shortcuts import render
from catalog.models import Category, Product

def category(request, category_id):
    template_name = 'category.html'
    data = {}

    page = request.GET.get('page', 1)

    data['category'] = Category.objects.get(pk=category_id)
    products = Product.objects.filter(categories__id=category_id).order_by('sort_order')
    paginator = Paginator(products, 10) 

    try:
        data['products'] = paginator.page(page)
    except PageNotAnInteger:
        data['products'] = paginator.page(1)
    except EmptyPage:
        data['products'] = paginator.page(paginator.num_pages)
    

    return render(request, template_name, data)

def product(request, category_id, product_id):
    template_name = 'product.html'
    data = {}
    data['category'] = Category.objects.get(pk=category_id)
    data['product'] = Product.objects.get(pk=product_id)
    return render(request, template_name, data)
