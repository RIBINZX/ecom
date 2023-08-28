from django.shortcuts import render

from .models import Product,Category,Product_images
from django.core.paginator import Paginator



# Create your views here.

    
    
def index(request):
    products=Product.objects.all()
    category=Category.objects.all()
    
    context={
        'products':products,
        'category':category
    }
    return render(request, 'index.html',context)
def shop(request):
    products = Product.objects.all()
    count = products.count()
    
    paginator = Paginator(products, 6) 
    page_number = request.GET.get('page')
    page_products = paginator.get_page(page_number)
    
    category=Category.objects.all()
    
    context = {
        "count": count,
        'page_products': page_products,
        'category': category,
    }
    return render(request, 'shop.html',context)

def product_details(request,id):
    products = Product.objects.get(id=id)
    
    product_images = Product_images.objects.filter(product=products)

    context = {      
        'product': products,
        'product_images': product_images
    }
    
    return render(request, 'product-details.html',context)

def category_shop(request,id):
    category = Category.objects.get(id=id) 
    
    # Filter products based on the selected category
    products = Product.objects.filter(category=category)
    
    paginator = Paginator(products, 8)  # Display 9 products per page
    page_number = request.GET.get('page')
    page_products = paginator.get_page(page_number)
    
    context = {
        'category': category,
        # 'products': products,
        'page_products': page_products,
    }
    return render(request, 'shop-grid.html', context)
