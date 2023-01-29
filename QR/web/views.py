from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from qr_code.qrcode.utils import MeCard


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect(home)
    else:
        return redirect(login_view)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(home)
    else:
        form = AuthenticationForm()
    return render(request, 'web/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect(index)


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            mobile = form.cleaned_data.get('mobile')
            organization = form.cleaned_data.get('organization')
            url = form.cleaned_data.get('url')

            user.userprofile.mobile = mobile
            user.userprofile.organization = organization
            user.userprofile.url = url

            user.userprofile.save()

            return redirect(login_view)
    else:
        form = CustomUserCreationForm()
    return render(request, 'web/signup.html', {'form': form})


def generate_vcard_from_user(user):
    vcard = MeCard(
        name=user.username,
        phone=user.userprofile.mobile,
        email=user.email,
        url=user.userprofile.url,
        org=user.userprofile.organization
    )

    return vcard


def public_page(request, username):
    if request.method == 'GET':
        try:
            user = User.objects.get(username=username)

            data = dict(
                vcard=generate_vcard_from_user(user),
                user=user,
            )

            return render(request, 'web/public_page.html', context=data)

        except User.DoesNotExist:
            return render(request, 'web/404.html', context={'username': username})


@login_required
def home(request):
    return render(request, 'web/home.html', context={'vcard': generate_vcard_from_user(request.user)})
