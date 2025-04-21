from django import forms
from .models import *
class PartnerForm(forms.ModelForm):
    rating = forms.DecimalField(min_value=0.0)
    class Meta:
        model = Partners
        exclude = ('partnerid',)