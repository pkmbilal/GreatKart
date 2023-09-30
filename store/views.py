from django.shortcuts import render, get_object_or_404
from store.models import Product
from category.models import Category

# Store Page
def store(request, category_slug=None):
    if category_slug:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        products_count = products.count()
        return render(request, 'store/store.html', {'products': products, 'products_count': products_count})
 
    products = Product.objects.filter(is_available=True)
    products_count = products.count()
    return render(request, 'store/store.html', {'products': products, 'products_count': products_count})

# Single Product Page
def product_detail(request, category_slug, product_slug):
    single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    context = {'single_product':single_product}
    return render(request, 'store/product-detail.html/',context)