from store.models import Product
from django.shortcuts import get_object_or_404, render
from category.models import Category

# Create your views here.

def store(request, category_slug=None):
    categories = None
    products = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        #paginator = Paginator(products, 2)
        #page = request.GET.get('page')
        #paged_products = paginator.get_page(page)
        product_count = products.count()
    else:        
        products = Product.objects.all().filter(is_available=True)
        #paginator = Paginator(products, 3)
        #page = request.GET.get('page')
        #paged_products = paginator.get_page(page)
        product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        #in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as e:
        raise e
    
    """if request.user.is_authenticated:
        try:
            orderproduct = OrderProduct.objects.filter(user=request.user, product_id=single_product.id).exists()
        except OrderProduct.DoesNotExist:
            orderproduct = None
    else:
        orderproduct = None

    # Get the reviews
    reviews = ReviewRating.objects.filter(product_id=single_product.id, status=True)

    # Obtener la galería de productos
    product_gallery = ProductGallery.objects.filter(product_id=single_product.id) """

    context = {
        'single_product': single_product,
        #'in_cart': in_cart,
        #'orderproduct': orderproduct,
        #'reviews': reviews,
        #'product_gallery': product_gallery,
    }
    return render(request, 'store/product_detail.html', context)
