from django.shortcuts import render, redirect
from. models import Product, Cart
from django.http import JsonResponse


def view_product(request):
    context = {}
    products = Product.objects.all()
    context["products"] = products
    return render(request, "product/products.html", context)







def product_detail(request, prod_id):
    context = {}
    product = Product.objects.get(id=prod_id)
    context["product"] = product
    return render(request, "product/product_detail.html", context)





def add_to_cart(request):
    current_user = request.user
    if request.method == "POST":
        if request.user.is_authenticated:
            product_id = int(request.POST.get("product_id"))
            product_check = Product.objects.get(id=product_id)
            if product_check:
                if Cart.objects.filter(user=current_user, product_id=product_id):
                    return JsonResponse({"status":"Product is Already in Cart"})
                else:
                    product_qyt = 1
                    Cart.objects.create(user=current_user, product_id=product_id, quantity=product_qyt)
                    return JsonResponse({"status":"product added successfuly"})
            else:
                return JsonResponse({"status": "no such Product found!"})
        else:
            return JsonResponse({"status": "Login to countinue"})
    return redirect("/")
