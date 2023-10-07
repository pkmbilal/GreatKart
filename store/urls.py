from django.urls import path
from .import views

urlpatterns = [
    # Store page
    path('',views.store,name='store'),

    # Filter by category
    path('<slug:category_slug>/',views.store,name='products_by_category'),

    # Single Product Page
    path('<slug:category_slug>/<slug:product_slug>/',views.product_detail,name='product_detail'),
]