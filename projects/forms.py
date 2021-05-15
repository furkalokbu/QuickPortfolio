from django import forms
from .models import Portfolio


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Portfolio
        fields = ('title', 'image')