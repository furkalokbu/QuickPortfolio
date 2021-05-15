from django.shortcuts import render
from .forms import ImageForm
import requests
from django.conf import settings
from .models import Portfolio


# def image_upload_view(request):
#     """Process images uploaded by users"""
#     portfolios = Portfolio.objects.all()
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # Get the current instance object to display in the template
#             img_obj = form.instance
#             return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
#     else:
#         form = ImageForm()
#     return render(request, 'index.html', {'form': form, 'image_all': Portfolio.objects.all()})


def Home(request):
    template_name = "index.html"
    portfolios = Portfolio.objects.all()
    context = {'portfolios': portfolios}

    response = requests.get('http://104.236.5.177/api/portfolio/')
    # response = requests.get('http://localhost:8000/api/portfolio/')

    if response.status_code == 200:
        context = {"portfolios": response.json(),}
    else:
        context = {
            "portfolios": {},
            "error": "Bad response!"}
  
    return render(request, template_name, context)


def PortfolioDetail(request, pk):
    template_name = "detail.html"
    try:
        detail = Portfolio.objects.filter(pk=pk).first()
        return render (request, template_name, {'detail': detail})
    except Portfolio.DoesNotExist:
        return None

