from django.shortcuts import render,HttpResponseRedirect
from .models import Cart,CartItem,Order,OrderItem
from products.models import Product
from .forms import OrderForm
import uuid
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from superpet.settings import EMAIL_HOST_USER
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login")
def add_to_cart (request,productId):
    CurentUser=request.user
    cart,created=Cart.objects.get_or_create(user=CurentUser)
    request.session["cart_id"]=cart.id


    quantity=request.GET.get("quantity")

    product=Product.manager.get(id=productId)

    cartitem,created=CartItem.objects.get_or_create(cart=cart,product=product)
    cartitem.quantity+=int(quantity)
    cartitem.save()
    

    #print(cart,creted)
    return HttpResponseRedirect("/products")



#login required
@login_required(login_url="/login")
def cart(request):
    cart,created=Cart.objects.get_or_create(user=request.user)
    cartitems=cart.cartitem_set.all()
    request.session["cart_id"]=cart.id

    total=0
    for cartitem in cartitems:
        total+=cartitem.quantity*cartitem.product.product_price

    return render(request,"cart.html",{"cartitems":cartitems,"total":total}) 

@login_required(login_url="/login")
def remove_from_card(request,cartItemId):
    cartitem=CartItem.objects.get(id=cartItemId)
    cartitem.delete()
    return HttpResponseRedirect("/cart")


@login_required(login_url="/login")
def update_cart(request,cartItemId):
    quantity=request.GET.get("quantity")
    cartitem=CartItem.objects.get(id=cartItemId)
    cartitem.quantity=quantity
    cartitem.save()
    return HttpResponseRedirect("/cart")


@login_required(login_url="/login")
def checkout(request):
    if request.method=="GET":
        data={"first_name":request.user.first_name,"last_name":request.user.last_name}
        form=OrderForm(initial=data)
        return render(request,"checkout.html",{"form":form})
    if request.method=="POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            order=Order.objects.create(order_id=uuid.uuid4().hex,user=request.user,
                                 first_name=form.cleaned_data["first_name"],
                                 last_name=form.cleaned_data["last_name"],
                                 phoneno=form.cleaned_data["phoneno"],
                                 address_line1=form.cleaned_data["address_line1"],
                                 address_line2=form.cleaned_data["address_line2"],
                                 city=form.cleaned_data["city"],
                                 state=form.cleaned_data["state"],
                                 pincode=form.cleaned_data["pincode"])
            cart=Cart.objects.get(id=request.session.get("cart_id"))
            for cartitem in cart.cartitem_set.all():
                OrderItem.objects.create(order=order,
                                         product=cartitem.product,
                                         quantity=cartitem.quantity)
            return HttpResponseRedirect("/cart/payment/"+order.order_id)

#================================make payment========================
@login_required(login_url="/login")
def payment(request,orderId):
    order=Order.objects.get(order_id=orderId)
    amount=0
    for orderitem in order.orderitem_set.all():
        amount+=orderitem.product.product_price*orderitem.quantity

    client=razorpay.Client(auth=("rzp_test_vUuRGMVovGGIMN"	,"0ANDRfXioZ3rCUGQA0z8SR5N"))
    data={"amount":amount*100,"currency":"INR","receipt":orderId}
    payment=client.order.create(data=data)
    print(payment)
    return render(request,"payment.html",{"payment":payment})

@csrf_exempt
def success(request,orderId):
    client=razorpay.Client(auth=("rzp_test_vUuRGMVovGGIMN"	,"0ANDRfXioZ3rCUGQA0z8SR5N"))
    paymentCheck=client.utility.verify_payment_signature({
        "razorpay_order_id":request.POST.get("razorpay_order_id"),
        "razorpay_payment_id":request.POST.get("razorpay_payment_id"),
        "razorpay_signature":request.POST.get("razorpay_signature")
    })

    if paymentCheck:
            order=Order.objects.get(order_id=orderId)
            order.paid=True
            order.save()
            cart=Cart.objects.get(user=request.user)
            cart.delete()

            #send_mail("order Placed")
            send_mail("order Placed",#subject
                      "thank you placing order",#message
                      EMAIL_HOST_USER,#sender
                      ["veeramanikaniccfc@gmail.com"],#reciver
                      fail_silently=False
                      )

            




            return render(request,"success.html")
            

