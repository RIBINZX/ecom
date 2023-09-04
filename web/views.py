from django.shortcuts import render

from .models import Product,Category,Product_images,Review
from django.core.paginator import Paginator
from .forms import ReviewForm
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required 



# Create your views here.

    
@login_required  
def index(request):
    products=Product.objects.all()
    category=Category.objects.all()
    
    context={
        'products':products,
        'category':category
    }
    return render(request, 'index.html',context)



@login_required
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


@login_required
def product_details(request,id):
    products = Product.objects.get(id=id)
    
    product_images = Product_images.objects.filter(product=products)
    
    related_products = Product.objects.filter(category=products.category).exclude(id=id)
    
    reviews = Review.objects.filter(product=products)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = products
            
            # Set the user's email and name from the logged-in user
            review.email = request.user.email
            review.name = request.user.username
            
            review.save()
            form = ReviewForm()  # Reset the form after submission
    else:
        form = ReviewForm()

    context = {      
        'product': products,
        'product_images': product_images,
        'related_products':related_products,
        'review_form': form,
        'reviews': reviews

    }
    
    return render(request, 'product-details.html',context)


@login_required
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
