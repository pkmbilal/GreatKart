from django.shortcuts import render, get_object_or_404
from store.models import Product
from category.models import Category
from carts.models import CartItem
from carts.views import _cart_id
from django.core.paginator import Paginator
from django.db.models import Q

# Store Page
def store(request, category_slug=None):
    if category_slug:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True).order_by('id')
        # Paginator for Category
        paginator = Paginator(products, 1)
        page = request.GET.get('page')
        paged_product = paginator.get_page(page)
        products_count = products.count()
        return render(request, 'store/store.html', {'products': paged_product, 'products_count': products_count})
    else:
        products = Product.objects.filter(is_available=True).order_by('id')
        # Paginator for all products
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_product = paginator.get_page(page)
        products_count = products.count()
        return render(request, 'store/store.html', {'products': paged_product, 'products_count': products_count})

# Single Product Page
def product_detail(request, category_slug, product_slug):
    single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    context = {
        'single_product':single_product,
        'in_cart':in_cart,
        }
    return render(request, 'store/product-detail.html/',context)

# Search Page
def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
    products_count = products.count()
    context = {'products': products, 'products_count': products_count}
    return render(request, 'store/store.html', context)