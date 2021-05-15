from django.shortcuts import render
import requests
from django.conf import settings
from .models import Image, Portfolio, Comments
from .forms import FeedbackRequestForm
from django.template.loader import render_to_string
from django.http import JsonResponse

def Home(request):
    template_name = "index.html"
    portfolios = Portfolio.objects.all()
    context = {'portfolios': portfolios}

    # response = requests.get(settings.SERVER_IP + 'api/portfolio/')

    # if response.status_code == 200:
    #     context = {"portfolios": response.json(),}
    # else:
    #     context = {
    #         "portfolios": {},
    #         "error": "Bad response!"}
  
    return render(request, template_name, context)


def PortfolioDetail(request, pk):
    template_name = "detail.html"
    
    template = "includes/comments.html"
    
    try:
        detail = Portfolio.objects.filter(pk=pk).first()
        images = Image.objects.filter(portfolio=detail)
        comments = Comments.objects.filter(portfolio=detail)    
    except Portfolio.DoesNotExist:
        return None 

    form = FeedbackRequestForm()
    success = False
    
    if request.method == 'POST':
        form = FeedbackRequestForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            # img_obj = form.instance
            form = FeedbackRequestForm()
        else:
            print(form.errors)

    else:
        form = FeedbackRequestForm()

    return render (request, template_name, {'detail': detail, 'images': images, 'form': form, 'comments': comments})