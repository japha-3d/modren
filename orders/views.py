from django.shortcuts import render, get_object_or_404
from ecommerce_website.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from datetime import datetime

# datetime object containing current date and time

from .models import OrderItem, Order, Product
from .forms import OrderCreateForm
from cart.views import get_cart, cart_clear
from decimal import Decimal
from cart.forms import CartAddProductForm
def order_create(request):
    
    cart = get_cart(request)
    product_ids = cart.keys()
    products = Product.objects.filter(id__in=product_ids)
    temp_cart = cart.copy()

    for product in products:
        cart_item = temp_cart[str(product.id)]
        cart_item['product'] = product
        cart_item['total_price'] = (Decimal(cart_item['price'])
                                    * cart_item['quantity'])
        cart_item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': cart_item['quantity']
        })
    
    cart_total_price =int(sum(Decimal(item['price']) * item['quantity']
                        for item in temp_cart.values()))
    cart_qty = sum(item['quantity'] for item in cart.values())
    transport_cost =product.delivery_charges
    if request.method == 'POST':
        
        color=request.POST.get('color')
        size=request.POST.get('size')
        order_form = OrderCreateForm(request.POST)
        if order_form.is_valid():
            cf = order_form.cleaned_data
            transport = cf['transport']
            email=cf['email']
            first_name=cf['first_name']
            last_name=cf['last_name']
            telephone=cf['telephone']
            address=cf['address']
            if transport == 'Recipient pickup':
                transport_cost = 0
            order = order_form.save(commit=False)
            order.transport_cost = Decimal(transport_cost)
            order.save()
            
            product_ids = cart.keys()
            products = Product.objects.filter(id__in=product_ids)
            for product in products:
                cart_item =cart[str(product.id)]
                price=eval(cart_item['price'])
                quantity=(cart_item['quantity'])
                total=(price*quantity)+transport_cost
                OrderItem.objects.create(order=order,product=product,price=cart_item['price'],quantity=cart_item['quantity'])
                subject = f'Order number is {order.id}'
                time=datetime.now()
                dt_string = time.strftime("%d/%m/%Y %H:%M:%S")
                
                message = f'Name: {first_name}{last_name} \nTelephone: {telephone}\nAdress: {address}\nproduct: {product}\nQuantity: {quantity}\nColor:{color}\nSize: {size}\nprice: {price}\nDelivery_Charges: {transport_cost}\nTotal_Bill: {total}\nDatetime: {dt_string}'
                recepient_list = ['huzaifaafzal259@gmail.com']
                send_mail(subject, 
                message, EMAIL_HOST_USER, recepient_list, fail_silently = False)

            cart_clear(request)
            return render(
            request,
            'order_created.html',
            {'order': order}
            )
    else:
        order_form = OrderCreateForm()
    return render(
    request,'order_create.html',{'cart':cart,'order_form':order_form,'transport_cost':transport_cost,"product":product,}
    )