from django import forms
from django.forms import ModelForm
from ads.models import VehicleModel, Matter, Color
from ads.models import Piece
from ads.models import Picture
from ads.models import Ad
from ads.models import Category
from ads.models import Brand


class  VehicleForm(ModelForm):
    class Meta:
        model= VehicleModel
        fields='__all__'

    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['model'] = forms.CharField()

class PieceForm(ModelForm):
    class Meta:
        model= Piece
        fields='__all__'

    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['references'] = forms.CharField()

class BrandForm(ModelForm):
    class Meta:
        model= Brand
        fields='__all__'


class MatterForm(ModelForm):
    class Meta:
        model= Matter
        fields='__all__'

class ColorForm(ModelForm):
    class Meta:
        model= Color
        fields='__all__'

class PictureForm(ModelForm):
    class Meta:
        model= Picture
        fields='__all__'
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['filename'] = forms.CharField()

class AdForm(ModelForm):
    class Meta:
        model= Ad
        fields='__all__'
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['name'] = forms.CharField()
        self.fields['title'] = forms.CharField()
        self.fields['description'] = forms.CharField()

class CategoryForm(ModelForm):
    class Meta:
        model= Category
        fields='__all__'


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Nom d utilisateur')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')




