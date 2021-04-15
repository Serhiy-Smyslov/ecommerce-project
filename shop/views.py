from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def home(request, category_slug=None):
    """Get information products by their category."""
    category_page = None
    products = None
    if category_slug:
        category_page = get_object_or_404(Category, slug=category_slug)
        # check availability category
        products = Product.objects.all().filter(category=category_page,
                                                available=True)
    else:
        products = Product.objects.all().filter(available=True)
    return render(request, 'home.html', {
        'products': products,
        'category': category_page,
    })


def product(request, category_slug, product_slug):
    """Get information about product."""
    try:
        shop_product = Product.objects.get(category__slug=category_slug,
            slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'product.html', {
        'product': shop_product,
    })


def _cart_id(request):
    """Check user session and return its key."""
    cart = request.session.session_key
    if not cart:
        cart = request.session.create() # create new session
    return cart


def add_cart(request, product_id):
    """Add products or create product in user cart."""
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product, quantity=1,
                                            cart=cart)
        cart_item.save()
    return redirect('cart_detail')  # Redirect on next function


def cart_detail(request, counter=0, total=0, card_id=None):
    """Get detail about client order."""
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart,
                                             active=True)
        for cart_item in cart_items:  # Count sum and amount of product
            total += cart_item.product.price * cart_item.quantity
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total,
        'counter': counter,
    })