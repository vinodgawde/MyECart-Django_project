from django.shortcuts import render, HttpResponseRedirect
from . models import Contact, Orders, Product
from math import ceil
from .forms import SignUpform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

def index(request):
    if request.user.is_authenticated:
        allProds = []
        catprods = Product.objects.values('category', 'id')
        cats = {item['category'] for item in catprods}
        for cat in cats:
            prod = Product.objects.filter(category=cat)
            n = len(prod)
            nSlides = (n // 4 + ceil((n / 4) - (n // 4))) + 1
            allProds.append([prod, range(1, nSlides), nSlides])
        params = {'allProds':allProds}
        return render(request, 'shop/index.html', params)
    else:
        return HttpResponseRedirect('/shop/login/')

def about(request):
    if request.user.is_authenticated:
    
        return render(request,'shop/about.html',{})
    else:
        return HttpResponseRedirect('/shop/login/')
    

def contact(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            title = request.POST.get('title','')
            msg = request.POST.get('msg','')
            contact = Contact(name=name, email=email, title=title, msg=msg)
            contact.save()
        return render(request,'shop/contact.html',{})
    else:
        return HttpResponseRedirect('/shop/login/')

def tracker(request):
    if request.user.is_authenticated:
        return render(request,'shop/tracker.html',{})
    else:
        return HttpResponseRedirect('/shop/login/')

def searchMatch(query, item):
        if query in item.product_desc.lower() or query in item.product_name.lower() or query in item.category.lower():
            return True
        else:
            return False

def search(request):
    if request.user.is_authenticated:
        query = request.GET.get('search')
        allProds = []
        catprods = Product.objects.values('category', 'id')
        cats = {item['category'] for item in catprods}
        for cat in cats:
            prodtemp = Product.objects.filter(category=cat)
            prod = [item for item in prodtemp if searchMatch(query, item)]

            n = len(prod)
            nSlides = n // 4 + ceil((n / 4) - (n // 4))
            if len(prod) != 0:
                allProds.append([prod, range(1, nSlides), nSlides])
        params = {'allProds': allProds, "msg": ""}
        if len(allProds) == 0:
            params = {'msg': "Search item is not found..."}
        return render(request, 'shop/search.html', params)
    else:
        return HttpResponseRedirect('/shop/login/')


def productview(request,myid):
    if request.user.is_authenticated:
        product = Product.objects.filter(id=myid)
        return render(request,'shop/productview.html',{'product':product[0]})
    else:
        return HttpResponseRedirect('/shop/login/')

def checkout(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            items_json = request.POST.get('itemJson','')
            name = request.POST.get('name','')
            phone = request.POST.get('phone','')
            email = request.POST.get('email','')
            address = request.POST.get('address1','') + request.POST.get('address2','')
            city = request.POST.get('city','')
            state = request.POST.get('state','')
            zip_code = request.POST.get('zip_code','')
            order = Orders(items_json=items_json, name=name, phone=phone, email=email, address=address, city=city, state=state, zip_code=zip_code)
            order.save()
            thank=True
            id= order.order_id
            return render(request,'shop/checkout.html',{'thank':thank, 'id':id })
        return render(request,'shop/checkout.html',{})
    else:
        return HttpResponseRedirect('/shop/login/')

def signup(request):
    if request.method=='POST':
        fm = SignUpform(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = SignUpform()
    return render(request,'shop/signup.html',{'form' : fm})

def u_login(request):
    if request.method=='POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/shop/')
    else:
        fm = AuthenticationForm()
    return render(request,'shop/login.html',{'form' : fm})

def u_logout(request):
    logout(request)
    return HttpResponseRedirect('/shop/login/')

def guest(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = (n // 4 + ceil((n / 4) - (n // 4))) + 1
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, 'shop/guest.html', params)

def gabout(request):
    return render(request,'shop/gabout.html',{})

def gcontact(request):
    if request.method=='POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        title = request.POST.get('title','')
        msg = request.POST.get('msg','')
        contact = Contact(name=name, email=email, title=title, msg=msg)
        contact.save()
    return render(request,'shop/gcontact.html',{})

def gproductview(request,myid):
    product = Product.objects.filter(id=myid)
    return render(request,'shop/gproductview.html',{'product':product[0]})


