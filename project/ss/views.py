from django.shortcuts import render, redirect , HttpResponse , HttpResponseRedirect
from .models import *
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cart.cart import Cart
import random
import razorpay
# Create your views here.


#user
@login_required(login_url='/')
def abo(r):
    men = 1
    women = 2
    mcategor = ProductsName.objects.filter(id=men)
    wcategor = ProductsName.objects.filter(id=women)
    context = {
        'mcategory': mcategor,
        'wcategory': wcategor,
    }
    return render(r, 'about.html', context)


@login_required(login_url='/')
def con(r):
    men = 1
    women = 2
    mcategor = ProductsName.objects.filter(id=men)
    wcategor = ProductsName.objects.filter(id=women)
    context = {
        'mcategory': mcategor,
        'wcategory': wcategor,
    }
    return render(r, 'contact.html', context)




@login_required(login_url='/')
def ind(r):
    if r.user.is_authenticated:
        men = 1
        women = 2
        mcategor = ProductsName.objects.filter(id=men)
        wcategor = ProductsName.objects.filter(id=women)
        kurthas = Product.objects.filter(category_id=10)
        shirts = Product.objects.filter(category_id=2)
        shoes = Product.objects.filter(category_id=3)
        watches = Product.objects.filter(category_id=5)
        coun = User.objects.all()
        count = len(coun)
        context = {
            'count':count,
            'mcategory': mcategor,
            'wcategory': wcategor,
            'Kurthas': kurthas,
            'Shirts': shirts,
            'Shoes': shoes,
            'Watches': watches,
        }
        return render(r, 'index.html', context)
    return render(r, 'index.html')


@login_required(login_url='/')
def sin(r):
    return render(r, 'single.html')


@login_required(login_url='/')
def typo(request):
    if request.user.is_authenticated:
        men = 1
        women = 2
        mcategor = ProductsName.objects.filter(id=men)
        wcategor = ProductsName.objects.filter(id=women)
        username = User.objects.get(id=request.user.id)
        order = Order.objects.filter(user=username).order_by('-date')
        res = ResAddress.objects.filter(username=username)
        ress = ShiAddress.objects.filter(username=username)
        context = {
            'mcategory': mcategor,
            'wcategory': wcategor,
            'resident': res,
            'shipping': ress,
            'order':order,
        }
        return render(request, 'typographly.html', context)
    return render(request, 'typographly.html')


@login_required(login_url='/')
def mproduct_detail(r):
    categoryid = r.GET.get('category')
    category = r.GET.get('categorys')
    subid=r.GET.get('subid')
    suboff=r.GET.get('suboff')
    off=r.GET.get('off')
    men = 1
    women = 2
    flatdiscount = suboffer.objects.get(name='Flat Discounts Men', offername__name='Best offer Men')
    summerdiscount = suboffer.objects.get(name='Summer Discount men', offername__name='Best offer Men')
    per40 = suboffer.objects.get(name='40% Men', offername__name='Best offer Men')
    per50 = suboffer.objects.get(name='50% Men', offername__name='Best offer Men')
    newarrival = suboffer.objects.get(name='New Arrival Mens', offername__name='Best offer Men')
    ATOZID = r.GET.get('ATOZ')
    ZTOAID = r.GET.get('ZTOA')
    PRICELowTOHigh=r.GET.get('PRICELowTOHigh')
    PRICEHighTOLow=r.GET.get('PRICEHighTOLow')
    offer = offername.objects.filter(id=1)
    soffer = suboffer.objects.filter(id=1)
    soffer1 = suboffer.objects.filter(id=2)
    soffer2 = suboffer.objects.filter(id=7)
    soffer3 = suboffer.objects.filter(id=5)
    soffer4 = suboffer.objects.filter(id=9)
    cat=categoryid
    cats = category
    mcategor = ProductsName.objects.filter(id=men)
    wcategor = ProductsName.objects.filter(id=women)
    if categoryid:
        products = Product.objects.filter(category=categoryid)
    elif subid  and suboff and off:
        if subid == 'None' and suboff == 'None' and off == 'None':
            if ATOZID and cats and subid and suboff and off:
                if cats == 'None':
                    products = Product.objects.filter(productsname_id=men).order_by('name')
                else:
                    products = Product.objects.filter(category=cats, productsname_id=men).order_by('name')
            elif ZTOAID and cats and subid and suboff and off:
                if cats == 'None':
                    if subid == 'None' and suboff == 'None' and off == 'None':
                        products = Product.objects.filter(productsname_id=men).order_by('-name')
                    else:
                        products = Product.objects.filter(category=subid, suboffer=suboff, offername=off).order_by('-name')
                else:
                    if subid == 'None' and suboff == 'None' and off == 'None':
                        products = Product.objects.filter(category=cats, productsname_id=men).order_by('-name')
                    else:
                        products = Product.objects.filter(category=cats, productsname_id=men).order_by('-name')
            elif PRICELowTOHigh and cats and subid and suboff and off:
                if cats == 'None':
                    if subid == 'None' and suboff == 'None' and off == 'None':
                        products = Product.objects.filter(productsname_id=men).order_by('price')
                    else:
                        products = Product.objects.filter(category=subid, suboffer=suboff, offername=off).order_by('price')
                else:
                    if subid == 'None' and suboff == 'None' and off == 'None':
                        products = Product.objects.filter(category=cats, productsname_id=men).order_by('price')
                    else:
                        products = Product.objects.filter(category=cats, productsname_id=men).order_by('price')
            elif PRICEHighTOLow and cats and subid and suboff and off:
                if cats == 'None':
                    if subid == 'None' and suboff == 'None' and off == 'None':
                        products = Product.objects.filter(productsname_id=men).order_by('-price')
                    else:
                        products = Product.objects.filter(category=subid, suboffer=suboff, offername=off).order_by('-price')
                else:
                    if subid == 'None' and suboff == 'None' and off == 'None':
                        products = Product.objects.filter(category=cats, productsname_id=men).order_by('-price')
                    else:
                        products = Product.objects.filter(category=cats, productsname_id=men).order_by('-price')
        else:
            if ATOZID is None and ZTOAID is None and PRICELowTOHigh is None and PRICEHighTOLow is None:
                products = Product.objects.filter(category=subid, suboffer=suboff, offername=off)
            elif ATOZID and  cats == 'None':
                products =Product.objects.filter(category=subid, suboffer=suboff, offername=off).order_by('name')
            elif ZTOAID and  cats == 'None':
                products =Product.objects.filter(category=subid, suboffer=suboff, offername=off).order_by('-name')
            elif PRICELowTOHigh and  cats == 'None':
                products =Product.objects.filter(category=subid, suboffer=suboff, offername=off).order_by('price')
            elif PRICEHighTOLow and  cats == 'None':
                products =Product.objects.filter(category=subid, suboffer=suboff, offername=off).order_by('-price')
    else:
        products = Product.objects.filter(productsname_id=men)
    context = {
        'flatdiscount': flatdiscount,
        'summerdiscount': summerdiscount,
        'newarrival': newarrival,
        'per50': per50,
        'per40': per40,
        'cat':cat,
        'cats':cats,
        'subid':subid,
        'suboff':suboff,
        'off':off,
        'soffer4': soffer4,
        'soffer2': soffer2,
        'soffer3': soffer3,
        'soffer1': soffer1,
        'soffer': soffer,
        'offer':offer,
        'mcategory': mcategor,
        'wcategory': wcategor,
        'products': products,
    }
    return render(r, 'mens.html', context)


@login_required(login_url='/')
def wproduct_detail(r):
    categoryid = r.GET.get('category')
    category = r.GET.get('categorys')
    subid = r.GET.get('subid')
    suboff = r.GET.get('suboff')
    off = r.GET.get('off')
    men = 1
    women = 2
    flatdiscount=suboffer.objects.get(name='Flat Discounts Women',offername__name='Best offer Women')
    summerdiscount=suboffer.objects.get(name='Summer Discount w',offername__name='Best offer Women')
    per40 = suboffer.objects.get(name='40% Women', offername__name='Best offer Women')
    per50 = suboffer.objects.get(name='50% Women', offername__name='Best offer Women')
    newarrival = suboffer.objects.get(name='New Arrival Womens', offername__name='Best offer Women')
    ATOZID = r.GET.get('ATOZ')
    ZTOAID = r.GET.get('ZTOA')
    PRICELowTOHigh = r.GET.get('PRICELowTOHigh')
    PRICEHighTOLow = r.GET.get('PRICEHighTOLow')
    offer = offername.objects.filter(id=4)
    soffer = suboffer.objects.filter(id=3)
    soffer1 = suboffer.objects.filter(id=4)
    soffer2 = suboffer.objects.filter(id=8)
    soffer3 = suboffer.objects.filter(id=6)
    soffer4 = suboffer.objects.filter(id=10)
    cat = categoryid
    cats = category
    mcategor = ProductsName.objects.filter(id=men)
    wcategor = ProductsName.objects.filter(id=women)
    if categoryid:
        products = Product.objects.filter(category=categoryid)
    elif subid and suboff and off:
        if subid == 'None' and suboff == 'None' and off == 'None':
            if ATOZID and cats and subid and suboff and off:
                if cats == 'None':
                    products = Product.objects.filter(productsname_id=women).order_by('name')
                else:
                    products = Product.objects.filter(category=cats, productsname_id=women).order_by('name')
            elif ZTOAID and cats and subid and suboff and off:
                if cats == 'None':
                    if subid == 'None' and suboff == 'None' and off == 'None':
                        products = Product.objects.filter(productsname_id=women).order_by('-name')
                    else:
                        products = Product.objects.filter(category=subid, suboffer=suboff, offername=off).order_by(
                            '-name')
                else:
                    if subid == 'None' and suboff == 'None' and off == 'None':
                        products = Product.objects.filter(category=cats, productsname_id=women).order_by('-name')
                    else:
                        products = Product.objects.filter(category=cats, productsname_id=women).order_by('-name')
            elif PRICELowTOHigh and cats and subid and suboff and off:
                if cats == 'None':
                    if subid == 'None' and suboff == 'None' and off == 'None':
                        products = Product.objects.filter(productsname_id=women).order_by('price')
                    else:
                        products = Product.objects.filter(category=subid, suboffer=suboff, offername=off).order_by(
                            'price')
                else:
                    if subid == 'None' and suboff == 'None' and off == 'None':
                        products = Product.objects.filter(category=cats, productsname_id=women).order_by('price')
                    else:
                        products = Product.objects.filter(category=cats, productsname_id=women).order_by('price')
            elif PRICEHighTOLow and cats and subid and suboff and off:
                if cats == 'None':
                    if subid == 'None' and suboff == 'None' and off == 'None':
                        products = Product.objects.filter(productsname_id=women).order_by('-price')
                    else:
                        products = Product.objects.filter(category=subid, suboffer=suboff, offername=off).order_by(
                            '-price')
                else:
                    if subid == 'None' and suboff == 'None' and off == 'None':
                        products = Product.objects.filter(category=cats, productsname_id=women).order_by('-price')
                    else:
                        products = Product.objects.filter(category=cats, productsname_id=women).order_by('-price')
        else:
            if ATOZID is None and ZTOAID is None and PRICELowTOHigh is None and PRICEHighTOLow is None:
                products = Product.objects.filter(category=subid, suboffer=suboff, offername=off)
            elif ATOZID and cats == 'None':
                products = Product.objects.filter(category=subid, suboffer=suboff, offername=off).order_by('name')
            elif ZTOAID and cats == 'None':
                products = Product.objects.filter(category=subid, suboffer=suboff, offername=off).order_by('-name')
            elif PRICELowTOHigh and cats == 'None':
                products = Product.objects.filter(category=subid, suboffer=suboff, offername=off).order_by('price')
            elif PRICEHighTOLow and cats == 'None':
                products = Product.objects.filter(category=subid, suboffer=suboff, offername=off).order_by('-price')
    else:
        products = Product.objects.filter(productsname_id=women)
    context = {
        'flatdiscount':flatdiscount,
        'summerdiscount':summerdiscount,
        'newarrival':newarrival,
        'per50':per50,
        'per40':per40,
        'cat':cat,
        'cats':cats,
        'soffer4':soffer4,
        'subid':subid,
        'suboff':suboff,
        'soffer2':soffer2,
        'soffer3':soffer3,
        'off':off,
        'soffer1': soffer1,
        'soffer': soffer,
        'offer':offer,
        'mcategory': mcategor,
        'wcategory': wcategor,
        'products': products,
    }
    return render(r, 'womens.html', context)



@login_required(login_url='/')
def prod_detail_page(r):
    id = r.GET.get('cat')
    prod = Product.objects.filter(id=id).first()
    data1 = Product.objects.filter(id=7).first()
    data2 = Product.objects.filter(id=3).first()
    data3 = Product.objects.filter(id=6).first()
    data4= Product.objects.filter(id=8).first()
    var= Size.objects.filter(product=id)
    men = 1
    women = 2
    mcategor = ProductsName.objects.filter(id=men)
    wcategor = ProductsName.objects.filter(id=women)
    context = {
        'mcategory': mcategor,
        'wcategory': wcategor,
        'prod': prod,
        'var':var,
        'data1':data1,
        'data2': data2,
        'data3': data3,
        'data4': data4,
    }
    return render(r, 'single.html', context)

# def adminsignupuser(request):
#     if request.user.is_authenticated:
#         return redirect(adminn)
#     else:
#         if request.method == 'POST':
#             username = request.POST['User_Name']
#             email = request.POST['Email']
#             password = request.POST['password']
#             lastname = request.POST['last_name']
#             firstname = request.POST['first_name']
#             data = User.objects.create_user(username=username, email=email, first_name=firstname, last_name=lastname, password=password)
#             if data is not None:
#                 data.is_superuser = True
#                 data.save()
#             return render(request, 'registration/login.html')
#
#         return render(request, 'registration/adminreg.html')
def signupuser(request):
    if request.user.is_authenticated:
        return redirect(abo)
    else:
        context = {}
        if request.method == 'POST':
            username = request.POST['User_Name']
            email = request.POST['Email']
            password = request.POST['password']
            lastname = request.POST['last_name']
            firstname = request.POST['first_name']
            cpassword = request.POST['confirmpassword']
            if cpassword == password:
                try:
                    data = User.objects.create_user(username=username, email=email, first_name=firstname, last_name=lastname, password=password)
                    data.save()
                    return render(request, 'registration/login.html')
                except:
                    context['msz'] = "Username is already exsist"
                    context['col'] = "alert-warning"
                    return render(request, 'registration/register.html',context)
            else:
                context['msz'] = "Password Missmatch"
                context['col'] = "alert-warning"
                return render(request, 'registration/register.html', context)
        return render(request, 'registration/register.html')


def loginuser(request):
    if request.user.is_authenticated:
        return redirect(abo)
    else:
        context = {}
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user is not None and user.is_superuser:
                    login(request, user)
                    return redirect(adminn)
                else:
                    login(request, user)
                    return redirect(abo)
            else:
                context['msz'] = "Username or Password Wrong"
                context['col'] = "alert-warning"
        return render(request, 'registration/login.html', context)


@login_required(login_url='/')
def logoutuser(request):
    logout(request)
    return redirect(loginuser)


@login_required(login_url='/')
def addaddressship(request):
    if request.method == 'POST':
        house = request.POST['house']
        locality = request.POST['locality']
        district = request.POST['District']
        pincode = request.POST['pincode']
        username = User.objects.get(id=request.user.id)
        usr = User.objects.get(username=username)
        data = ShiAddress.objects.create(housename=house, area=locality,  district=district,  pincode=pincode, username=usr)
        data.save()
        return redirect(typo)
    return render(request, 'shipadd.html')


@login_required(login_url='/')
def addaddressres(request):
    if request.method == 'POST':
        house = request.POST['house']
        locality = request.POST['locality']
        district = request.POST['District']
        pincode = request.POST['pincode']
        username = User.objects.get(id=request.user.id)
        usr = User.objects.get(username=username)
        data = ResAddress.objects.create(housename=house, area=locality, district=district, pincode=pincode, username=usr)
        data.save()
        return redirect(typo)

    return render(request, 'resadd.html')


@login_required(login_url='/')
def residentedit(request):
    if request.method == 'POST':
        house = request.POST['house']
        locality = request.POST['locality']
        district = request.POST['District']
        pincode = request.POST['pincode']
        user = User.objects.get(id=request.user.id)
        usr = User.objects.get(username=user)
        ResAddress.objects.update(housename=house, area=locality, district=district, pincode=pincode, username=usr)
        return redirect(typo)

    return render(request, 'resaddressedit.html')


@login_required(login_url='/')
def shippingedit(request):
    if request.method == 'POST':
        house = request.POST['house']
        locality = request.POST['locality']
        district = request.POST['District']
        pincode = request.POST['pincode']
        user = User.objects.get(id=request.user.id)
        usr = User.objects.get(username=user)
        ShiAddress.objects.update(housename=house, area=locality, district=district, pincode=pincode, username=usr)
        return redirect(typo)

    return render(request, 'shipaddressedit.html')

@login_required(login_url='/')
def error(r):
    return render(r,'Admtemp/404.html')


@login_required(login_url='/')
def detailsedit(request):
    context = {}
    if request.method == 'POST':
        oldpassword = request.POST['cpassword']
        newpassword = request.POST['newpassword1']
        user = User.objects.get(id=request.user.id)
        un = user.username
        chec = user.check_password(oldpassword)
        if chec is True:
            user.set_password(newpassword)
            user.save()
            context['msz'] = "password changed succesfully"
            context['col'] = "alert-success"
            user = User.objects.get(username=un)
            login(request, user)
            messages.success(request, "Password Changed Successfully")
            return redirect(typo)
        else:
            messages.error(request, "Password is Wrong")
            return redirect(typo)


@login_required(login_url='/')
def profileedit(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['eemail']
        user = User.objects.get(id=request.user.id)
        if user is not None:
            user.email =email
            user.first_name =first_name
            user.last_name =last_name
            user.save()
            messages.success(request, "Profile Edited Successfully")
            return redirect(typo)
        else:
            messages.error(request, "Something Went Wrong")
            return redirect(typo)

@login_required(login_url='/')
def complaint(r):
    if r.method=='POST':
        email = r.POST['Email']
        subject = r.POST['Subject']
        message = r.POST['Message']
        userr = User.objects.get(id=r.user.id)
        user = User.objects.get(username=userr)
        data = Complaint.objects.create(user=user,email=email,subject=subject,message=message)
        data.save()
        return render(r, 'contact.html')
    else:
        return redirect(con)



#CART___________________________________________________________________________________


@login_required(login_url='/')
def cart_add(request, id):
    if request.method=='POST':
        sise=request.POST['sise']
        cart = Cart(request)
        product = Product.objects.get(id=id)
        c=product.id
        siSe = Size.objects.get(product=c,name=sise)
        cart.add(product=product,variant=siSe,sise=sise)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/')
def item_clear(request, id):
    product = Size.objects.get(id=id)
    cart = Cart(request)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url='/')
def item_increment(request):
    id = request.GET.get('id')
    sise = request.GET.get('sise')
    cart = Cart(request)
    product = Product.objects.get(id=id)
    c = product.id
    siSe = Size.objects.get(product=c, name=sise)
    cart.add(product=product,variant=siSe,sise=sise)
    return redirect("cart_detail")


@login_required(login_url='/')
def item_decrement(request):
    id = request.GET.get('id')
    sise = request.GET.get('sise')
    cart = Cart(request)
    product = Product.objects.get(id=id)
    c = product.id
    siSe = Size.objects.get(product=c, name=sise)
    cart.decrement(product=product,variant=siSe,sise=sise)
    return redirect("cart_detail")


@login_required(login_url='/')
def cart_detail(request):
    username = User.objects.get(id=request.user.id)
    ress = ShiAddress.objects.filter(username=username)
    men = 1
    women = 2
    mcategor = ProductsName.objects.filter(id=men)
    wcategor = ProductsName.objects.filter(id=women)
    cart = Cart(request)
    total_bill = 0.0
    for key, value in request.session['cart'].items():
        total_bill = total_bill + (float(value['price']) * value['quantity'])
    amount = total_bill*100
    currency = "INR"
    callback_url = redirect(checkout)
    notes = { 'order-type': "basic order from website",'key':'value'}
    client = razorpay.Client(auth=("rzp_test_HBfXehKNxLWnK1", "SMJn6PpzFYwvJyZRocxj0TAD"))
    if amount>0:
        payment_order = client.order.create({'amount': amount, 'currency': currency, 'notes':notes ,'payment_capture': 1})
        payment_order_id = payment_order['id']
        order_status=payment_order['status']
        if order_status == 'created':
            payment=Payment(
                user = username,
                amount = amount,
                orderid =payment_order_id,
                status_pay =order_status
            )
            payment.save()
        context = {
            'callback_url':callback_url,
            'amount': amount,
            'API_KEY': "rzp_test_HBfXehKNxLWnK1",
            'orderid': payment_order_id,
            'shipping': ress,
            'mcategory': mcategor,
            'wcategory': wcategor,

        }
    else:
        context = {
            'shipping': ress,
            'mcategory': mcategor,
            'wcategory': wcategor,
        }
    return render(request, 'cart.html',context)


@login_required(login_url='/')
def Search(request):
    men = 1
    women = 2
    mcategor = ProductsName.objects.filter(id=men)
    wcategor = ProductsName.objects.filter(id=women)
    query = request.GET['query']
    product = Product.objects.filter(category__name__icontains=query)
    if product:
        context = {
            'mcategory': mcategor,
            'wcategory': wcategor,
                'prod': product,
        }
    else:
        product = Product.objects.filter(name__icontains=query)
        context = {
            'mcategory': mcategor,
            'wcategory': wcategor,
            'prod': product,
        }
    return render(request, 'search.html', context)

#checkout


@login_required(login_url='/')
def checkout(request):
    order_id = request.GET.get('orderid')
    cart = request.session.get('cart')
    userr = User.objects.get(id=request.user.id)
    address = ShiAddress.objects.get(username=userr)
    user = User.objects.get(username=userr)
    payment = Payment.objects.get(orderid=order_id)

    payment.paid=True
    payment.save()
    for i in cart:
        a=(int(cart[i]['price']))
        b=(int(cart[i]['quantity']))
        trck = random.randint(100000000, 999999999)
        order=Order(
            user=user,
            product=cart[i]['name'],
            price=cart[i]['price'],
            quantity=cart[i]['quantity'],
            image=cart[i]['image'],
            size=cart[i]['size'],
            address=address,
            total=a*b,
            orderid=trck,
            payment=payment
        )
        order.save()
        request.session['cart'] = {}
    return redirect(ind)

#Admtemp
@login_required(login_url='/')
def adminn(r):
    if r.user.is_superuser:
        coun = User.objects.all()
        prod = Product.objects.all()
        produ =len(prod)
        count=len(coun)
        return render(r, 'Admtemp/index.html',{'count':count,'produ':produ})
    else:
        return redirect(error)


@login_required(login_url='/')
def men(r):
    if r.user.is_superuser:
        nameid = 1
        products = Product.objects.filter(productsname_id=nameid)
        context = {
            'products': products,
        }
        return render(r, 'Admtemp/mens.html', context)
    else:
        return redirect(error)

@login_required(login_url='/')
def women(r):
    if r.user.is_superuser:
        nameid = 2
        products = Product.objects.filter(productsname_id=nameid)
        context = {
            'products': products,
        }
        return render(r, 'Admtemp/womens.html', context)
    else:
        return redirect(error)

@login_required(login_url='/')
def user(r):
    if r.user.is_superuser:
        usr = User.objects.all()
        return render(r, 'Admtemp/user.html',{'user':usr})
    else:
        return redirect(error)

@login_required(login_url='/')
def userdelete(r):
    if r.user.is_superuser:
        id = r.GET.get('cat')
        User.objects.get(id=id).delete()
        return render(r, 'Admtemp/index.html')
    else:
        return redirect(error)

@login_required(login_url='/')
def order(r):
    if r.user.is_superuser:
        filte= r.GET.get('query')
        if filte:
            order = Order.objects.filter(orderid=filte)
        else:
            order = Order.objects.all()
        return render(r, 'Admtemp/orders.html',{'order':order})
    else:
        return redirect(error)

@login_required(login_url='/')
def editadmin(r):
    if r.user.is_superuser:
        id = r.GET.get('cat')
        products = Product.objects.filter(id=id)
        if r.method == 'POST':
            context={}
            variant = r.POST.getlist('sise')
            dvariant = r.POST.getlist('sises')
            id = r.POST['idprod']
            name = r.POST['name']
            Price = r.POST['price']
            dprice = r.POST['dprice']
            image1 = r.FILES['img1']
            brand = r.POST['brand']
            image2 = r.FILES['img2']
            image3 = r.FILES['img3']
            description = r.POST['description']
            prod = Product.objects.get(id=id)
            prod.name=name
            prod.image = image1
            prod.image1 = image2
            prod.image2 = image3
            prod.brand = brand
            prod.price=Price
            prod.dprice = dprice
            prod.description=description
            prod.save()

            for i in variant:
                Size.objects.get_or_create(name=i,product=prod)
            for i in dvariant:
                try:
                    Size.objects.get(name=i, product=prod).delete()
                except:
                    context['msz'] = "No Item with selected Variant found"
                    context['col'] = "alert-warning"

            return render(r, 'Admtemp/index.html',context)
        return render(r,'Admtemp/editprod.html',{'products':products})
    else:
        return redirect(error)

@login_required(login_url='/')
def deleteadmin(r):
    if r.user.is_superuser:
        id = r.GET.get('cat')
        Product.objects.get(id=id).delete()
        return HttpResponseRedirect(r.META.get('HTTP_REFERER'))
    else:
        return redirect(error)

@login_required(login_url='/')
def addprod(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            variant=request.POST.getlist('sise')
            section = request.POST['Section']
            if section == 'Men':
                offer = 'Best offer Men'
            else:
                offer = 'Best offer Women'
            suboffe = request.POST['Offer']
            catego = request.POST['Category']
            name = request.POST['name']
            Price = request.POST['price']
            dprice = request.POST['dprice']
            brand = request.POST['brand']
            image1 = request.FILES['img1']
            image2 = request.FILES['img2']
            image3 = request.FILES['img3']
            description = request.POST['description']
            prod = Product.objects.filter(productsname__name=section, category__name=catego,offername__name=offer,suboffer__name=suboffe)
            productname =  ProductsName.objects.get(name=section)
            Offer= offername.objects.get(name = offer)
            subofferr = suboffer.objects.get(name=suboffe)
            categor = category.objects.get(name=catego)
            data = Product.objects.create(category=categor,brand=brand,offername=Offer,suboffer=subofferr,productsname=productname,image=image1, image1=image2,image2=image3,name=name,dprice=dprice,price=Price,description=description)
            for i in variant:
                Size.objects.create(name=i,product=data)

            return redirect(adminn)

        return render(request, 'Admtemp/AddProduct.html')
    else:
        return redirect(error)

@login_required(login_url='/')
def sscomplaint(r):
    if r.user.is_superuser:
        data=Complaint.objects.all()
        return render(r, 'Admtemp/complaints.html',{'message':data})
    else:
        return redirect(error)

@login_required(login_url='/')
def sscomplaintview(r):
    if r.user.is_superuser:
        id = r.GET.get('cat')
        if id:
            data=Complaint.objects.get(id=id)
            mesg=data.message
            return render(r, 'Admtemp/complaintview.html',{'message':mesg})
        else:
            return redirect(sscomplaint)
    else:
        return redirect(error)

@login_required(login_url='/')
def productview(r):
    if r.user.is_authenticated:
        id = r.GET.get('order')
        product = Order.objects.filter(id=id)
        username = User.objects.get(id=r.user.id)
        order = Order.objects.filter(id=id,user=username)
        details = orderdetailadmin.objects.filter(ids=id)
        context={
            'details':details,
            'order':order,
            'product':product
        }
    return render(r,'Productstatuss.html',context)

@login_required(login_url='/')
def ordercancel(r):
    if r.user.is_authenticated:
        id = r.GET.get('order')
        username = User.objects.get(id=r.user.id)
        order=Order.objects.get(id=id,user=username)
        if order.status==False:
            order.delete()
            messages.success(r, "Order Cancelled successfully")
            return redirect(typo)
        else:
            messages.error(r, "Order is approved by admin.For cancel you need to request to admin through complaint in 'Contact' page")
            return redirect(typo)
    else:
        return redirect(login)

@login_required(login_url='/')
def trackprovide(r):
    if r.user.is_superuser:
        id = r.GET.get('order')
        product = Order.objects.filter(id=id)
        username = User.objects.get(id=r.user.id)
        order = Order.objects.filter(id=id, user=username)
        context = {
            'order': order,
            'product': product,
        }
    return render(r, 'Admtemp/trackprovide.html',context)



@login_required(login_url='/')
def ordertrack(r):
    if r.user.is_superuser:
        if r.method == 'POST':
            ids = r.POST['id']
            deliverypartner = r.POST['deliverypartner']
            deliverydate = r.POST['date']
            trck=random.randint(100000000,999999999)
            trck=orderdetailadmin.objects.create(ids=ids,deliverypartner=deliverypartner,deliverydate=deliverydate,trackid=trck)
            trck.save()
            statu = Order.objects.get(id=ids)
            statu.status=True
            statu.save()
            return redirect(order)
        else:
            return redirect(trackprovide)
    else:
        return redirect(error)

@login_required(login_url='/')
def orderstatus(r):
    if r.user.is_authenticated:
        id = r.GET.get('order')
        product = Order.objects.filter(id=id)
        orders = Order.objects.get(id=id)
        details = orderdetailadmin.objects.filter(ids=id)

        context = {
            'orders':orders,
            'details': details,
            'product': product
        }
    return render(r, 'Admtemp/statusupdate.html',context)




@login_required(login_url='/')
def orderstatusmain(r):
    if r.user.is_authenticated:
        Picked = r.GET.get('Picked')
        Ontheway = r.GET.get('Ontheway')
        Ready = r.GET.get('Ready')
        Cancel = r.GET.get('Cancel')
        subid = r.GET.get('subid')
        if subid:
            order = Order.objects.get(id=subid)
            if Picked:
                order.picked = True
                order.save()
            elif Ontheway:
                order.picked = True
                order.otw = True
                order.save()
            elif Ready:
                order.picked = True
                order.otw = True
                order.pickup = True
                order.save()
            elif Cancel:
                orderdetailadmin.objects.get(ids=subid).delete()
                Order.objects.get(id=subid).delete()
        return redirect(adminn)
