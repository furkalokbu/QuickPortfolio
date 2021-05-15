from django.utils.translation import ugettext_lazy as _
import os
from django.conf import settings
from django.db import models

# from djlime.utils import get_file_path
# from imagekit.models.fields import ImageSpecField
# from imagekit.processors.resize import ResizeToFill

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio/%Y/%m/%d/', blank=True)


    def __str__(self):
        return self.title

# class Portfolio(models.Model):

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     show = models.BooleanField(_("show"), default=True)
#     title = models.CharField(max_length=200)
#     description = models.TextField(_("description"), blank=True)
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     main_image = models.ImageField(
#         _("main image"),
#         upload_to='portfolio/%Y/%m/%d/',
#         null=True,
#         blank=True,
#     )
#     large = ImageSpecField([ResizeToFill(930, 310)], source="main_image")
#     thumbnail = ImageSpecField([ResizeToFill(360, 320)], source="main_image")


#     def get_absolute_image(self):
#         return os.path.join('/media', self.main_image.name)
    
#     def image_url(self):
#         return self.thumbnail.url


#     class Meta:
#         ordering = ("created_at",)
#         verbose_name = _("Portfolio")

#     def __str__(self):
#         return self.author.username


# class Image(models.Model):

#     created_at = models.DateTimeField(auto_now_add=True)
#     enabled = models.BooleanField(_("enabled"), default=True)
#     title = models.CharField(_("name"), max_length=100)
#     portfolio = models.ForeignKey(
#         Portfolio, null=True, on_delete=models.SET_NULL, verbose_name=_("portfolio")
#     )
#     image = models.ImageField(
#         _("image"),
#         upload_to='images',
#         help_text=_("recommended size 1000x665"),
#         null=True,
#         blank=True,
#     )

#     large = ImageSpecField([ResizeToFill(930, 310)], source="image")
#     thumbnail = ImageSpecField([ResizeToFill(360, 320)], source="image")


#     def __str__(self):
#         return self.title
