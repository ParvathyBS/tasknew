from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from .models import Branch, Sub_Branch


# Create your views here.
def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "INVALID CREDENTIALS")
            return redirect('login')

    return render(request, "login.html")


def register(request):
    # b = Background.objects.all()
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        cp = request.POST['cpassword']

        if p == cp:
            if User.objects.filter(username=u).exists():
                messages.info(request, "Username already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=u, password=p)
                user.save()
                return redirect('taskapp/login')
        else:
            messages.info("PASSWORD NOT MATCHING")
            return redirect('register')

    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def allBranch(request, c_slug=None):
    c_page = None
    products_list = None
    # products = None
    if c_slug != None:
        c_page = get_object_or_404(Branch, slug=c_slug)
        branch = Branch.objects.all().filter(bch=c_page, available=True)
    else:
        branch = Branch.objects.all().filter(available=True)

    return render(request, 'branch.html', {'bch': c_page})


def formfill(request):
    return render(request, 'form.html')


def subbranch(request, c_slug, sub_slug):
    try:
        s = Sub_Branch.objects.get(branch__slug=c_slug, slug=sub_slug)
    except Exception as e:
        raise e
    return render(request, 'product.html', {'s': s})


def printform(request):
    print(request.POST)
    return render(request, "form.html")
