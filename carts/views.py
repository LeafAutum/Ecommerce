from django.shortcuts import render, redirect
from products.models import Product
from .models import Cart
# Create your views here.
# def cart_create(user=None):
#
#   cart_obj= Cart.objects.create(user=None)
#   print("New cart created")
#   return cart_obj
def cart_update(request):
    print(request.POST.get('product_id'))
    product_id=request.POST.get('product_id')
    if product_id is not None:
      try:
        product_obj = Product.objects.get(id=product_id)
      except Product.DoesNotExist:
        print("HI user product is gone ")
        return redirect("cart:home")
      cart_obj, new_obj = Cart.objects.new_or_get(request)
      if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
      else:
            cart_obj.products.add(product_obj)
      request.session['cart_items']= cart_obj.products.count()        
        #return redirect(product_obj.get_absolute_url())
    return redirect("cart:home")

def cart_home(request):
         cart_obj, new_obj =Cart.objects.new_or_get(request)
         # products= cart_obj.products.all()
         # total = 0
         # for x in products:
         #     total += x.price
         # print(total)
         # cart_obj.total =total
         #cart_obj.save()
         return render(request,"carts/home.html",{"cart":cart_obj})
    #del request.session['cart_id']
        #request.session['cart_id']= '12'
        # cart_id = request.session.get("cart_id", None)
        #         # if cart_id is None : #and isinstance(cart_id, int):
        #
        #         #     print("create new cart")
        #         #
        #         #     cart_obj =cart_create()
        #         #     print(cart_obj.id,cart_obj)
        #         #     request.session['cart_id'] = cart_obj.id
        #         # else:
        # qs=Cart.objects.filter(id=cart_id)
        # if qs.count()==1:
        #     print("cart ID exists")
        #     Cart_obj =qs.first()
        #     if request.user.is_authenticated and Cart_obj.user is None:
        #         Cart_obj.user = request.user
        #         Cart_obj.save()
        # else:
        #     Cart_obj =Cart.objects.new(user=request.user)
        #     request.session['cart_id'] = C art_obj.id

    #print(request.session)
    #print(dir(request.session))
    #request.session.set_expiry()
    # key = request.session.session_key
    # print(key)

    #request.session['user']=request.user.username
