from .models import Cart, CartItem
from .views import _cart_id

def counter(request):
    cart_count = 0
    cart = Cart.objects.filter(cart_id=_cart_id(request)).first()
    cart_items = CartItem.objects.filter(cart=cart)
    for cart_item in cart_items:
        cart_count += cart_item.quantity
    return dict(cart_count=cart_count)