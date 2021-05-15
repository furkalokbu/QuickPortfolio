from django.utils.translation import ugettext_lazy as _
import os
from django.conf import settings
from django.db import models
from imagekit.models.fields import ImageSpecField
from imagekit.processors.resize import ResizeToFill

class Portfolio(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    show = models.BooleanField(_("show"), default=True)   
    title = models.CharField(max_length=200)
    description = models.TextField(_("description"), blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio/%Y/%m/%d/', blank=True)
  
    large = ImageSpecField([ResizeToFill(930, 310)], source="image")
    thumbnail = ImageSpecField([ResizeToFill(360, 321)], source="image")

    class Meta:
        ordering = ("created_at",)
        verbose_name = _("Portfolio")

    def __str__(self):
        return self.author.username



class Image(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    enabled = models.BooleanField(_("enabled"), default=True)
    title = models.CharField(_("name"), max_length=100)

    portfolio = models.ForeignKey(
        Portfolio, null=True, on_delete=models.SET_NULL, related_name='portfolio')
        
    image = models.ImageField(upload_to='portfolio/%Y/%m/%d/', blank=True)

    large = ImageSpecField([ResizeToFill(930, 310)], source="image")
    thumbnail = ImageSpecField([ResizeToFill(360, 320)], source="image")


    def __str__(self):
        return self.title
