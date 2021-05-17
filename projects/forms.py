from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Comments, Portfolio, Image


class FeedbackRequestForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('message', 'name', 'email')
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': _('Your Name'), }
            ),
            'email': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': _('Your Email'), }
            ),
            'message': forms.Textarea(
                attrs={'rows': 5,'class': 'form-control', 'placeholder': _('Your Message'), }
            ),                        
        }

    def is_valid(self, *args, **kwargs):
        ret = super(FeedbackRequestForm, self).is_valid(*args, **kwargs)
        if ret is False:
            for f in self.fields:
                if f in self.errors:
                    self.fields[f].widget.attrs.update({'class': self.fields[f].widget.attrs.get('class', '') + ' is-invalid'})
                else:
                    if self.cleaned_data[f]:
                        self.fields[f].widget.attrs.update({'class': self.fields[f].widget.attrs.get('class', '') + ' is-valid'})
        return ret


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ('title', 'description', 'image')
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': _('Title'), }
            ),
            'description': forms.Textarea(
                attrs={'rows': 5,'class': 'form-control', 'placeholder': _('Description portfolio'), }
            ),                        
        }

    def is_valid(self, *args, **kwargs):
        ret = super(PortfolioForm, self).is_valid(*args, **kwargs)
        if ret is False:
            for f in self.fields:
                if f in self.errors:
                    self.fields[f].widget.attrs.update({'class': self.fields[f].widget.attrs.get('class', '') + ' is-invalid'})
                else:
                    if self.cleaned_data[f]:
                        self.fields[f].widget.attrs.update({'class': self.fields[f].widget.attrs.get('class', '') + ' is-valid'})
        return ret

class SearchForm(forms.Form):
    query = forms.CharField()

class ImageLoadForm(forms.ModelForm):
    
    class Meta:
        model = Image
        fields = ('title', 'portfolio', 'image')
    
    def __init__(self,user,*args,**kwargs):
        super (ImageLoadForm,self ).__init__(*args,**kwargs) # populates the post
        self.fields['portfolio'] = forms.ModelChoiceField(queryset=Portfolio.objects.filter(author=user))

