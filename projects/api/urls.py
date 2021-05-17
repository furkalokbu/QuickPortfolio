from django.conf.urls import url, include
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from projects.api import views as pv

app_name ='portfolio'

router = DefaultRouter()
router.register(r"portfolio", pv.PortfolioListView)

urlpatterns = [
    path("", include(router.urls))
    # path("portfolio/", views.PortfolioListView.as_view(), name="portfolio_list"),
]
