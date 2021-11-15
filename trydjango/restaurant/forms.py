from django import forms
from django.db.models import fields 

from .models import Restuarant

class RestaurantForm(forms.ModelForm):
    post = forms.CharField()


class RestaurantForm2(forms.ModelForm):
    class Meta:
        model = Restuarant
        fields = [ 'name', 'description', 'price' ]