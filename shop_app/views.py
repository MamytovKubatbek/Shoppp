
from .models import *
from .serializers import ClothesSerializer
from rest_framework import generics
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .api import *
from collections import Counter
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.http.response import HttpResponsePermanentRedirect
from django.conf.urls import *
from django.http.response import HttpResponsePermanentRedirect
from django.shortcuts import redirect

# Create your views here.

class ClothesAPIList(generics.ListCreateAPIView):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer

class ClothesAPIUpdate(generics.UpdateAPIView):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer

class ClothesAPIDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer




def main(request):
    elec_session = request.session.get('elec_session', [])
    return render(request, 'index.html', {'zipped_lst':zipped_lst, 'elec_session':elec_session})


############# CART    

def addCart(request, id):

    cart_session = request.session.get('cart_session', [])
    cart_session.append(id)
    request.session['cart_session'] = cart_session
    return HttpResponseRedirect('/')

def cart(request):
    cart_session = request.session.get('cart_session', [])
    count_of_product = len(cart_session)
    products_cart =[]
    all_products_sum = 0
    for j in cart_session:
        for i in zipped_lst:
            if i[0] == j:
                products_cart.append(i)
                all_products_sum+=i[4]
    product = Counter(products_cart)
    lst = []
    for p, c in product.items():
        lst.append([p,c])
    return render(request, 'cart.html',{'count_of_product': count_of_product, 'all_products_sum': all_products_sum , 'lst':lst} )


def removeCart(request ,id):
    try:
        cart_session = request.session.get('cart_session', [])
        carts = []
        carts = cart_session
        carts.remove(id)
        request.session['cart_session'] = carts
        return HttpResponseRedirect('/cart')
    except:
        return HttpResponseRedirect('/cart')

############# Elected

def addElect(request, id):
    elec_session = request.session.get('elec_session', [])
    if id in elec_session:
        pass
    else:
        elec_session.append(id)
    request.session['elec_session'] = elec_session
    # return HttpResponseRedirect('/')
    return redirect()


def elected(request):
    elec_session = request.session.get('elec_session', [])
    count_of_product = len(elec_session)
    products_cart =[]
    for j in elec_session:
        for i in zipped_lst:
            if i[0] == j:
                products_cart.append(i)
        
    return render(request, 'heart.html',{'count_of_product': count_of_product, 'products_cart':products_cart} )


def removeElected(request ,id):
    elec_session = request.session.get('elec_session', [])
    carts = []
    carts = elec_session
    carts.remove(id)
    request.session['elec_session'] = carts
    return HttpResponseRedirect('/elected')


########## Sign-in Sign-up ##########


def signUp(request):
        if request.method == 'POST':
            user = UserCreationForm(request.POST)
            if user.is_valid():
                user.save()
                return HttpResponseRedirect('/')
        else:
            user = UserCreationForm()
        return render(request, 'auth.html', {'user': user})

def signin(request):
        try:
            if request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/')
            else:
                form = AuthenticationForm()
            return render(request, 'auth.html', {'user': form})
        except UnboundLocalError:
           pass

def signout(request):
        logout(request)
        return HttpResponseRedirect('/')


def more_title(request, id):
    title_pro = []
    brend_pro = []
    for i in zipped_lst:
        if i[0]==id:
            title_pro.append(i)

    for i in zipped_lst:
        if i[6]==title_pro[0][6]:
            brend_pro.append(i)
    
    return render(request, 'more_pro.html', {'title_pro': title_pro, 'brend_pro':brend_pro})    
        

###################   ORDER   ##################



def name_order(request):
    return render(request, 'order.html')



def order(request):
    order = Order()
    cart_session = request.session.get('cart_session', [])
    if request.method == 'POST':
        if cart_session:
            order.full_name = request.POST.get('full_name')
            order.email = request.POST.get('email')
            order.password = request.POST.get('password')
            order.address = request.POST.get('address')
            order.phone_number = request.POST.get('phone_number')
            name_products = []
            for j in cart_session:
                for i in zipped_lst:
                    if i[0] == j:
                        name_products.append(i)
            order.name_products = name_products
            order.save()
       
            request.session['cart_session'] = []
            return HttpResponseRedirect('/cart')
        else:
            return HttpResponseRedirect('/cart')
    return HttpResponseRedirect('/cart') 




