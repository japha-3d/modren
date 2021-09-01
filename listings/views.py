from django.db.models import query
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product,Review,Return
from .forms import ReviewForm
from django.views.generic import  CreateView
from cart.forms import CartAddProductForm
from django.urls import reverse_lazy

def product_list(request, category_slug=None):
    categories = Category.objects.all()
    requested_category = None
    products = Product.objects.all()

    if category_slug:
        requested_category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=requested_category)
    else:
        requested_category=None
        products=Product.objects.all()

    return render(
        request,
        'product/list.html',
        {
            'categories': categories,
            'requested_category': requested_category,
            'products': products
        }
    )

def product_detail(request,category_slug,product_slug):
    category=get_object_or_404(Category,slug=category_slug)
    product=get_object_or_404(Product,category_id=category.id,slug=product_slug)
    if request.method=="POST":
        review_form=ReviewForm(request.POST)
        if review_form.is_valid():
            cf=review_form.cleaned_data
            author_name=request.user
            Review.objects.create(product=product,author=author_name,rating=cf['rating'],text=cf['text'])
            return redirect('listings:product_detail',category_slug=category_slug,product_slug=product_slug)
    else:
        review_form = ReviewForm()
        cart_product_form = CartAddProductForm()

        return render(
            request,
            'product/detail.html',
            {
                'product': product,
                'review_form': review_form,
                'cart_product_form': cart_product_form
            }
        )


    return render(
        request,'product/detail.html',{'product':product,'review_form':review_form})
def search(request):
    query=request.GET['query']
    products=Product.objects.filter(name__icontains=query)
    
    return render(
        request,'product/search.html',{'products':products})
def trending(request):
    products=Product.objects.all()
    return render(
        request,'product/trending.html',{'products':products},
    )
def discounted(request):
    products=Product.objects.all()
    return render(
        request,"product/discount.html",{'products':products})
def gift(request):
    return render(request, "product/gift.html")
class return_policy(CreateView):
    model=Return 
    template_name='product/return.html'
    success_url=reverse_lazy('listings:product_list')
    fields='__all__'