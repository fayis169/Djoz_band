from django.shortcuts import render, redirect, HttpResponse
from User_side.models import regDB, bookDB, u_contactDB, feedbackDB, u_sign
from Admin_Panel.models import asignup
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.

def u_sign_up(request):
    return render(request, "u_sign up.html")

def save_usignup(request):
    if request.method == "POST":
        na = request.POST.get('name')
        u_na = request.POST.get('u_name')
        e = request.POST.get('email')
        ad = request.POST.get('ad')
        pas = request.POST.get('pas')
        mob = request.POST.get('mob')
        obj = u_sign(name=na, u_name=u_na, pas=pas, email=e, address=ad, mobile=mob)
        obj.save()
        messages.success(request, "sign in successfully...")
        return redirect(u_login)

def u_login(request):
    return render(request, "u_login.html")

def u_loged(request):
    if request.method == "POST":
        un = request.POST.get('u_name')
        ps = request.POST.get('pass')
        if u_sign.objects.filter(u_name=un, pas=ps).exists():
            request.session['u_name']=un
            request.session['pass']=ps
            messages.success(request, "Loging is success..")
            return redirect(u_home)
        else:
            messages.error(request, "somthing error pleas check again..")
            return redirect(u_login)
    messages.error(request, "somthing error pleas check again..")
    return redirect(u_login)



def u_home(request):
    data = asignup.objects.all()
    item = regDB.objects.all()
    return render(request, "u_home.html", {'data': data, 'item': item})

def u_contact(request):
    data = asignup.objects.all()
    return render(request, "u_contact.html", {'data': data})

def register(request):
    data = asignup.objects.all()
    messages.info(request, "Carefully Fill..")
    return render(request, "Register.html", {'data': data})

def saveregistration(request):
    if request.method == "POST":
        bn = request.POST.get('b_name')
        y = request.POST.get('year')
        mob = request.POST.get('tel')
        em = request.POST.get('email')
        loc = request.POST.get('loc')
        ct = request.POST.get('cat')
        im = request.FILES['image']
        at = request.POST.get('attach')
        ab = request.POST.get('about')
        au = request.FILES['audio']
        obj = regDB(band_name=bn, year=y, mobile=mob, email=em, cat=ct, image=im, link=at, comment=ab, audio=au, loc=loc)
        obj.save()
        messages.success(request, "Your Band Added Success")
        return redirect(u_home)

def about(request):
    data = asignup.objects.all()
    return render(request, "about.html", {'data': data})

def all_band(request):
    data = asignup.objects.all()
    item = regDB.objects.all()
    return render(request, "all_band.html", {'item': item, 'data': data})

def single_page(request, bandid):
    data = asignup.objects.all()
    single = regDB.objects.get(id=bandid)
    return render(request, "single_page.html", {'single': single, 'data': data})

def music(request):
    data = asignup.objects.all()
    item = regDB.objects.all()
    return render(request, "music.html", {'data': data, 'item': item})

def filter(request, cat):
    data = asignup.objects.all()
    filter = regDB.objects.filter(cat=cat)
    return render(request, "filter_page.html", {'data': data, 'filter': filter})

def test(request):
    test = regDB.objects.all()
    return render(request, "test.html", {'test': test})

def booking(request):
    if request.method == "POST":
        n = request.POST.get('name')
        bn = request.POST.get('b_name')
        bm = request.POST.get('b_mobile')
        be = request.POST.get('b_email')
        e = request.POST.get('email')
        l = request.POST.get('loc')
        cn = request.POST.get('c_num')
        obj = bookDB(name=n, b_name=bn, b_mobile=bm, b_email=be, email=e, loc=l, mobile=cn)
        obj.save()
        subject = "Djoz band Booking"
        messages =f'name :{n}\n Email :{e}\n Location :{l}\n Mobile :{cn}'
        from_email = 'muhammedfayiskk169@gmail.com'
        recipient_list=[be]
        send_mail(subject, messages, from_email, recipient_list, fail_silently=False)
        return redirect(u_home)

def savecontact(request):
    if request.method == "POST":
        na = request.POST.get('name')
        e = request.POST.get('email')
        web = request.POST.get('web')
        c = request.POST.get('comment')
        obj = u_contactDB(c_name=na, email=e, web=web, comment=c)
        obj.save()
        return redirect(u_contact)

def feedback(request):
    if request.method == "POST":
        bn = request.POST.get('b_name')
        e = request.POST.get('email')
        f = request.POST.get('feedback')
        obj = feedbackDB(b_name=bn, email=e, feedback=f)
        obj.save()
        return redirect(all_band)


