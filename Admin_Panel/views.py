from django.shortcuts import render, redirect
from User_side.models import regDB, feedbackDB, bookDB, u_contactDB
from Admin_Panel.models import asignup
from django.contrib import messages

# Create your views here.

def a_sign_up(request):
    return render(request, "sign up.html")

def save_asignup(request):
    if request.method == "POST":
        na = request.POST.get('name')
        u_na = request.POST.get('u_name')
        e = request.POST.get('email')
        ad = request.POST.get('ad')
        pas = request.POST.get('pas')
        mob = request.POST.get('mob')
        obj = asignup(name=na, u_name=u_na, pas=pas, email=e, address=ad, mob=mob)
        obj.save()
        messages.success(request, "sign is success.")
        return redirect(a_login)

def a_login(request):
    return render(request, "login.html")

def a_loged(request):
    if request.method == "POST":
        un = request.POST.get('u_name')
        ps = request.POST.get('pass')
        if asignup.objects.filter(u_name=un, pas=ps).exists():
            request.session['u_name']=un
            request.session['pas']=ps
            messages.success(request, "Login success..")
            return redirect(a_home)

        else:
            messages.error(request, "Somthing wrong pleas check again..")
            return redirect(a_login)
    messages.error(request, "Somthing Wrong pleas check again..")
    return redirect(a_login)

def a_logout(request):
    del request.session['u_name']
    del request.session['pas']
    return redirect(a_login)

def a_home(request):
    data = asignup.objects.all()
    book = bookDB.objects.all()
    counter = 0
    for i in book:
        counter = counter + 1
    # filter = asignup.objects.filter(username=request.session['u_name'])
    return render(request, "a_home.html", {'data': data, 'book': book, 'counter': counter})

def item(request):
    data = regDB.objects.all()
    book = bookDB.objects.all()
    counter = 0
    for i in book:
        counter = counter + 1
    return render(request, "item.html", {'data': data, 'book': book, 'counter': counter})

def delete_item(request, id):
    data = regDB.objects.get(id=id)
    data.delete()
    return redirect(item)

def display_user(request):
    data = asignup.objects.all()
    book = bookDB.objects.all()
    counter = 0
    for i in book:
        counter = counter + 1
    # data = asignup.objects.filter(u_name=request.session['u_name'])
    return render(request, "display_user.html", {'data': data, 'book': book, 'counter': counter})


def user_delete(request, id):
    data = asignup.objects.get(id=id)
    data.delete()
    return redirect(a_home)

def edituser(request, e):
    data = asignup.objects.get(id=e)
    book = bookDB.objects.all()
    counter = 0
    for i in book:
        counter = counter + 1
    return render(request, "edit_user.html", {'data': data, 'book': book, 'counter': counter})

def updateuser(request, u):
    if request.method == "POST":
        na = request.POST.get('name')
        u_na = request.POST.get('u_name')
        e = request.POST.get('email')
        ad = request.POST.get('address')
        pas = request.POST.get('pas')
        mob = request.POST.get('mob')
        asignup.objects.filter(id=u).update(name=na, u_name=u_na, pas=pas, email=e, address=ad, mob=mob)
        # messages.success(request, "Category Updeted Succesfully..")
        if asignup.objects.filter(u_name=u_na, pas=pas).exists():
            request.session['u_name'] = u_na
            request.session['pas'] = pas
        messages.success(request, "Update success..")
        return redirect(display_user)

def display_feedback(request):
    data = feedbackDB.objects.all()
    book = bookDB.objects.all()
    counter = 0
    for i in book:
        counter = counter + 1
    return render(request, "feedback.html", {'data': data, 'book': book, 'counter': counter})

def delete_feedback(request, id):
    data = feedbackDB.objects.get(id=id)
    data.delete()
    messages.success(request, "Deleted Successfully...")
    return redirect(display_feedback)

def display_booking(request):
    data = bookDB.objects.all()
    book = bookDB.objects.all()
    counter = 0
    for i in book:
        counter = counter + 1
    return render(request, "display_booking.html", {'data': data, 'book': book, 'counter': counter})

def delete_booking(request, id):
    data = bookDB.objects.get(id=id)
    data.delete()
    messages.success(request, "Deleted Successfully...")
    return redirect(display_booking)

def display_contact(request):
    data = u_contactDB.objects.all()
    book = bookDB.objects.all()
    counter = 0
    for i in book:
        counter = counter + 1
    return render(request, "display_contact.html", {'data': data, 'book': book, 'counter': counter})

def delete_contact(request, id):
    data = u_contactDB.objects.get(id=id)
    data.delete()
    messages.success(request, "Deleted Successfully..")
    return redirect(display_contact)
