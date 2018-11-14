from django.views.generic.base import View
from django.shortcuts import render, redirect
import time

from books.models import Art
from users.models import Cart, LineItem
from users import forms
from users.models import ProductOrder, OrderItemRelation


def CartView(request):
    user = request.session.get("muser")
    (total_price, product_list) = Cart.get_products(user)
    context = dict(
        user=user,
        total_price=total_price,
        product_list=product_list,
    )
    return render(request, 'view_cart.html', context)


def AddCart(request):
    art_id = int(request.GET.get("id", 0))
    if art_id == 0:
        return redirect('/')
    product = Art.objects.get(a_id=art_id)
    user = request.session.get("muser")
    Cart.add_product(product, user)
    return redirect('/')


def CleanCart(request):
    user = request.session.get("muser")
    LineItem.objects.filter(user=user.id).delete()
    return CartView(request)


def CartOrder(request):
    user = request.session.get("muser")
    (total_price, product_list) = Cart.get_products(user)
    order_form = forms.OrderForms()
    context = dict(
        user=user,
        total_price=total_price,
        product_list=product_list,
        form=order_form,
    )
    return render(request, "product_order.html", context=context)


def CartOrderSubmit(request):
    url = request.path
    print(f"OrderSubmitHandler submit ok {url}")
    if request.method == "POST":
        order_form = forms.OrderForms(data=request.POST)
        if not order_form.is_valid():
            return CartOrder(request)
        address = order_form.cleaned_data.get("address")
        pay_type = int(order_form.cleaned_data.get("pay_type"))
        phone = int(order_form.cleaned_data.get("phone"))
        order_id = int(round(time.time() * 1000))
        prod_order = ProductOrder(order_id=order_id, address=address, pay_type=pay_type, phone=phone)
        prod_order.save()
        user = request.session.get("muser")
        line_items = LineItem.objects.filter(user=user.id)
        [OrderItemRelation(line_item_id=int(line_item.id), product_order_id=prod_order.id).save() for line_item in
         line_items]
    return redirect('http://127.0.0.1:8001/pay/alipay')
