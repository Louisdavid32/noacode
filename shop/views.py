from django.shortcuts import render, redirect
from .models import Product, Command
from django.core.paginator import Paginator


def index(request):
    product_object = Product.objects.all()
    item_name = request.GET.get('item-name')
    if item_name != '' and item_name is not None:
        product_object = Product.objects.filter(title__icontains=item_name)
    parginator = Paginator(product_object, 6)
    page = request.GET.get('page')
    product_object = parginator.get_page(page)
    return render(request, 'shop/index.html', {'product_object':product_object})


def detail(request, myid):
    product_object = Product.objects.get(id=myid)
    return render(request, 'shop/detail.html', {'product': product_object})


def checkout(request):
    if request.method == 'POST':
        item = request.POST.get('items')
        name = request.POST.get('nom')
        mail = request.POST.get('email')
        address = request.POST.get('address')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        total = request.POST.get('total')
        zipcode = request.POST.get('zipcode')
        com = Command(items=item, name=name, email=mail, address=address, ville=ville, pays=pays, total=total, zipcode=zipcode)
        com.save()
        return redirect('confirmation')

    return render(request, 'shop/checkout.html');



def confimation(request):
    info = Command.objects.all()
    for item in info:
        name = item.name
    return render(request, 'shop/confirmation.html', {'name': name})