"""project URL Configuration

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
from ss import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loginuser),
    path('about', views.abo),
    path('contact', views.con),
    path('index', views.ind),
    path('mens', views.mproduct_detail),
    path('single', views.sin),
    path('typography', views.typo),
    path('womens', views.wproduct_detail),
    path('view', views.prod_detail_page),
    # path('asignup', views.adminsignupuser),
    path('signup', views.signupuser),
    path('logout', views.logoutuser, name='logout'),
    path('shipaddress', views.addaddressship),
    path('resaddress', views.addaddressres),
    path('resedit', views.residentedit),
    path('shipedit', views.shippingedit),
    path('dedit', views.detailsedit),
    path('proedit', views.profileedit),
    path('search',views.Search,name='search'),
    path('complaint',views.complaint),
    path('error',views.error),
    path('productview',views.productview),
    path('ordercancel',views.ordercancel),
    path('ordertrack',views.ordertrack),
    path('trackprovide',views.trackprovide),
    path('orderstatus',views.orderstatus),
    path('orderstatusmain',views.orderstatusmain),
    #checkout
    path('checkout',views.checkout),

    #cart
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('item_increment', views.item_increment, name='item_increment'),
    path('item_decrement', views.item_decrement, name='item_decrement'),
    path('cart', views.cart_detail, name='cart_detail'),


    #Admtemp
    path('ssadmin', views.adminn),
    path('ssmen', views.men),
    path('sswomen', views.women),
    path('ssicons', views.user),
    path('ssorder', views.order),
    path('sscategory', views.category),
    path('ssaddprod', views.addprod),
    path('ssedit', views.editadmin),
    path('ssdelete', views.deleteadmin),
    path('ssusrdelete', views.userdelete),
    path('sscomplaint', views.sscomplaint),
    path('sscomplaintview', views.sscomplaintview),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
