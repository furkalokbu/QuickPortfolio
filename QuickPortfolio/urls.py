
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from projects import views
from users.forms import CustomUserForm
from django_registration.backends.one_step.views import RegistrationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home),
    path(
        "accounts/register/",
        RegistrationView.as_view(
            form_class=CustomUserForm,
            success_url="/",
        ),
        name="django_registration_register",
    ),
    path('search/', views.portfolio_search, name='portfolio_search'),
    path("accounts/", include("django_registration.backends.one_step.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("portfolio/<pk>/", views.PortfolioDetail, name="portfolio_detail"),
    path("myportfolio/", views.MyPortfolio, name="my_portfolio"),
    path("myportfolio/add/", views.add_portfolio, name="add_portfolio"),
    path("myportfolio/upload/", views.upload_image, name="upload_image"),
    path("<item_id>/remove/", views.remove_portfolio, name='remove-portfolio'),
    # path("api/", include("users.api.urls")),
    path("api/", include("projects.api.urls", namespace="api")),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, 
                          document_root=settings.STATIC_ROOT)
   
