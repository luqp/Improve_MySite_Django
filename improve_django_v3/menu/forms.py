from django import forms
from django.forms.extras.widgets import SelectDateWidget

from .models import Menu, Item, Ingredient

class MenuForm(forms.ModelForm):

    class Meta:
        model = Menu
        exclude = ('created_date',)
    
    expiration_date = forms.DateTimeField(
        widget=forms.DateInput(format='%m/%d/%Y'),
        input_formats=('%m/%d/%Y',),
        required=False
    )