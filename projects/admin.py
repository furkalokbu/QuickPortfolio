from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Portfolio, Image


class ImagesInline(admin.StackedInline):
    model = Image
    extra = 1
    show_change_link = True


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "show")
    # list_editable = ("enabled", "position")
    inlines = [ImagesInline]

