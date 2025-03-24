from .models import Cart



def cart_count(request):
    context = {}
    cart_total = 0
    current_user = request.user
    if current_user.is_authenticated:
        cart_items = Cart.objects.filter(user = current_user)
        if cart_items:
            for item in cart_items:
                cart_total+=item.quantity
                context["cart_total"] = cart_total    


    else:
        context["cart_total"] = 0    

    return context    