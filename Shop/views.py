from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Contact, Orders,OrderUpdate
from math import ceil
import json


# Create your views here.


def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request, 'Shop/index.html', params)


def searchMatch(query,item):
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodTemp = Product.objects.filter(category=cat)
        prod = [item for item in prodTemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds,'msg':""}
    print(len(allProds))
    if len(allProds) == 0 or len(query) < 4:
        params = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'Shop/search.html', params)


def about(request):
    return render(request, 'Shop/about.html')

def contact(request):
    thank = False
    if request.method == "POST":
        print(request)
        name = request.POST.get('name','')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        print(name,email,phone,desc)
        cont = Contact(name=name,email=email,phone=phone,desc=desc)
        cont.save()
        thank = True
    return render(request, 'Shop/contact.html',{'thank':thank})
    # return HttpResponse("we are at contact")


# noinspection PyBroadException
def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id = orderId, email = email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id = orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.time_stm})
                    response = json.dumps({"status":"success","updates":updates,"itemsJson":order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"no item"}')
        except Exception:
            return HttpResponse('{"status":"error"}')
    return render(request, 'Shop/tracker.html')




def productView(request,myid):
    # fetch the product using id
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request,"Shop/prodView.html",{'product':product[0]})


def checkout(request):
    if request.method == 'POST':
        print(request)
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')

        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city, state=state,
                       zip_code=zip_code, phone=phone,amount=amount)

        order.save()
        update = OrderUpdate(order_id = order.order_id,  update_desc ="The Order Has Been Placed")
        update.save()
        thank = True
        id = order.order_id
        print(id)
        return render(request, 'Shop/checkout.html', context={'thank': thank, 'id': id})
    return render(request, 'Shop/checkout.html')

