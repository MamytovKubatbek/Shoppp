"""drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .settings import MEDIA_ROOT, MEDIA_URL
from shop_app.views import *
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),

    path('api/v1/Clothes', ClothesAPIList.as_view()),
    path('api/v1/ClothesList/<int:pk>', ClothesAPIUpdate.as_view()),
    path('api/v1/ClothesDetaill/<int:pk>', ClothesAPIDelete.as_view()),

    path('cart/', cart, name='cart'),
    path('addcart/<int:id>', addCart, name='addCart'),
    path('removeCart/<int:id>', removeCart, name='removeCart'),

    path('elected/', elected, name='elected'),
    path('addElect/<int:id>', addElect, name='addElect'),
    path('removeElected/<int:id>', removeElected, name='removeElected'),

    path('signUp/', signUp, name='signUP'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),

    path('more/<int:id>', more_title, name='more_title'),

    path('name_order/', name_order, name='name_order'),
    path('order/', order, name='order'),


    
]

urlpatterns += static(MEDIA_URL,document_root = MEDIA_ROOT)

