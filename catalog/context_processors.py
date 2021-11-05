from catalog.models import Category

def categories(request):

    items = Category.objects.filter(status=True)
    return {
        'items_categories': items
    }