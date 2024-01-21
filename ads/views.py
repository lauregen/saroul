from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse

from .models import VehicleModel
from .models import Piece
from .models import Color
from .models import Matter
from .models import Brand
from .models import Picture
from .models import Ad
from .forms import VehicleForm
from .forms import PieceForm
from .forms import BrandForm
from.forms import  MatterForm
from.forms import ColorForm
from.forms import PictureForm
from.forms import AdForm
from.forms import CategoryForm


def vehicle_list(request):
    vehicles = VehicleModel.objects.all()
    return render(request,'vehicle_list.html',{'vehicles': vehicles})

def piece_list(request):
    pieces = Piece.objects.all()
    return render(request,'piece_list.html',{'pieces': pieces})

def color_list(request):
    colors = Color.objects.all()
    return render(request, 'color_list.html', {'colors': colors})

def matter_list(request):
    matters = Matter.objects.all()
    return render(request, 'matter_list.html', {'matters': matters})

def brand_list(request, brand_type):
    brands = Brand.objects.filter(brand_type__iexact=brand_type)
    return render(request, 'brand_list.html', {'brands':brands})

def picture_list(request):
    pictures = Picture.objects.all()
    return render(request, 'picture_list.html', {'pictures':pictures})

def ad_list(request):
    ads = Ad.objects.all()
    return render(request, 'ad_list.html',{'ads':ads} )

def ad_detail(request,ad_id):
    ad = Ad.objects.get(id=ad_id)
    return render(request, 'ad_detail.html', {'ad':ad})


@login_required(login_url='login')
def vehicle_form(request):
    if request.method == "POST":
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('vehicle-list'))
        else:
            return render(request, 'vehicle_form.html', {'form': form})
    else:
        form = VehicleForm().as_p()
        return render(request, 'vehicle_form.html', {'form':form})

@login_required(login_url='login')
def piece_form(request):
    if request.method == "POST":
        form = PieceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('piece-list'))
        else:
            return render(request, 'piece_form.html', {'form': form})
    else:
            form = PieceForm().as_p()
            return render(request, 'piece_form.html', {'form':form})

@login_required(login_url='login')
def brand_form(request):
    if request.method == "POST":
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('brand-form'))
        else:
            return render(request, 'brand_form.html', {'form': form})
    else:
        form = BrandForm().as_p()
        return render(request, 'brand_form.html', {'form': form})

@login_required(login_url='login')
def matter_form(request):
        if request.method == "POST":
            form = MatterForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('matter-list'))
            else:
                return render(request, 'matter_form.html', {'form': form})
        else:
            form = MatterForm().as_p()
            return render(request, 'matter_form.html', {'form': form})

@login_required(login_url='login')
def color_form(request):
        if request.method == "POST":
            form = ColorForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('color-list'))
            else:
                return render(request, 'color_form.html', {'form': form})
        else:
            form = ColorForm().as_p()
            return render(request, 'color_form.html', {'form': form})

@login_required(login_url='login')
def picture_form(request):
        if request.method == "POST":
            form = PictureForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('picture-form'))
            else:
                return render(request, 'picture_form.html', {'form': form})
        else:
            form = PictureForm().as_p()
            return render(request, 'picture_form.html', {'form': form})

@login_required(login_url='login')
def ad_form(request):
    if request.method == "POST":
        form = AdForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ad-list'))
        else:
            return render(request, 'ad_form.html', {'form': form})
    else:
        form = AdForm().as_p()
        return render(request, 'ad_form.html', {'form': form})

@login_required(login_url='login')
def category_form(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('category-form'))
        else:
            return render(request, 'category_form.html', {'form': form})
    else:
        form = CategoryForm().as_p()
        return render(request, 'category_form.html', {'form': form})






def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('ad-form')  # Redirige vers la page d'accueil après la connexion réussie
        else:
            return render(request, 'login.html', {'error_message': 'Identifiant ou mot de passe incorrect'})
    else:
        user_form= UserCreationForm()
    return render(request, 'login.html',{'user_form':user_form})




def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Coucou {username}, votre compte a été créé avec succès !')
            return redirect('register')

    return render(request, 'registration/register.html', {'form': form})

