from django.urls import path

import authentication.views
from . import views
from.views import vehicle_list
from.views import piece_list
from.views import color_list
from .views import brand_list
from .views import matter_list
from .views import picture_list
from .views import ad_list, ad_detail
from .views import vehicle_form
from .views import piece_form
from .views import brand_form
from .views import matter_form
from. views import color_form
from. views import picture_form
from.views import  ad_form
from.views import  category_form


urlpatterns = [
    path('vehicles/',vehicle_list, name='vehicle-list'),
    path('pieces/',piece_list, name='piece-list'),
    path('colors/',color_list, name='color-list'),
    path('matters/',matter_list, name='matter-list'),
    path('brands/<str:brand_type>/',brand_list, name='brand-list'),
    path('pictures/',picture_list, name='picture-list'),
    path('ads/',ad_list, name='ad-list'),
    path("ad/<int:ad_id>/", ad_detail, name="ad-detail"),
    path('vehicle/form/',vehicle_form, name='vehicle-form'),
    path('piece/form/',piece_form, name='piece-form'),
    path('brand/form/', brand_form, name='brand-form'),
    path('matter/form/',matter_form, name='matter-form'),
    path('color/form/', color_form, name= 'color-form'),
    path('picture/form/',picture_form, name= 'picture-form'),
    path('ad/form/', ad_form, name= 'ad-form'),
    path('category/form/', category_form, name= 'category-form'),
    path('login/',views.login_page, name='login'),
    path('register/', views.register, name='register'),


]
