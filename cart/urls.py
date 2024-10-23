from django.urls import path
from .views import landing_page, cart_view, checkout_view, add_to_cart

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('cart/', cart_view, name='cart_view'),
    path('checkout/', checkout_view, name='checkout_view'),
        path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),  # New line

]
