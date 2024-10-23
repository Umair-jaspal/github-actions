# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, CartItem

def landing_page(request):
    products = Product.objects.all()  # Fetch all products
    return render(request, 'cart/landing_page.html', {'products': products})  # Pass products to template

def cart_view(request):
    cart_items = CartItem.objects.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total_price': total_price})

def checkout_view(request):
    cart_items = CartItem.objects.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart/checkout.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product)
    if not created:
        cart_item.quantity += 1  # Increment quantity if item already in cart
    cart_item.save()
    return redirect('cart_view')
