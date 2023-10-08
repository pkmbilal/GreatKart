from django.urls import path
from .import views

urlpatterns = [
    # Store page
    path('',views.store,name='store'),

    # Filter by category
    path('category/<slug:category_slug>/',views.store,name='products_by_category'),

    # Single Product Page
    path('category/<slug:category_slug>/<slug:product_slug>/',views.product_detail,name='product_detail'),

    # Search url
    path('search/',views.search,name='search'),
]