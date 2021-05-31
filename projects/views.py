from django.shortcuts import render, get_object_or_404, redirect
import requests
from django.conf import settings
from django.contrib.postgres.search import SearchVector
from .models import Image, Portfolio, Comments
from .forms import FeedbackRequestForm, PortfolioForm, SearchForm, ImageLoadForm
from django.template.loader import render_to_string
from django.http import JsonResponse

def Home(request):
    template_name = "index.html"
    # portfolios = Portfolio.objects.all()
    # context = {'portfolios': portfolios}

    # response = requests.get('http://127.0.0.1:8000/api/portfolio/')
    response = requests.get(settings.SERVER_IP + 'api/portfolio/')
    

    if response.status_code != 200:
        print("Status code: ", response.status_code)
        context = {
            "portfolios": {},
            "error": "Bad response!"}
    else:
        context = {"portfolios": response.json(),}
    
    return render(request, template_name, context)


def PortfolioDetail(request, pk):
    template_name = "detail.html"
    
    try:
        detail = Portfolio.objects.filter(pk=pk).first()
    except Portfolio.DoesNotExist:
        return None
    try:
        images = Image.objects.filter(portfolio=detail)
    except Image.DoesNotExist:
        return None 
    try:
        comments = Comments.objects.filter(portfolio=detail) 
        count = len(comments)  
    except Comments.DoesNotExist:
        return None

    form = FeedbackRequestForm()
    success = False
    
    if request.method == 'POST':
        form = FeedbackRequestForm(request.POST, request.FILES)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.portfolio = detail 
            comment.save()

            form = FeedbackRequestForm()
        # else:
        #     print(form.errors)

    else:
        form = FeedbackRequestForm()

    return render (request, template_name, {'detail': detail, 'images': images, 'form': form, 'comments': comments, 'count': count})


def MyPortfolio(request):
    template_name = "includes/my_portfolio.html"
    
    try:
        portfolios = Portfolio.objects.filter(author=request.user)
    except Portfolio.DoesNotExist:
        return None
    
    context = {'portfolios': portfolios}

    return render (request, template_name, context)


def remove_portfolio(request, item_id):
    portfolio =  get_object_or_404(Portfolio, id=item_id)
    portfolio.delete()

    return redirect('my_portfolio')

def add_portfolio(request):
    template_name = "includes/add_portfolio.html"

    form = PortfolioForm()  

    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            portfolio=form.save(commit=False)
            portfolio.author = request.user
            portfolio.save()
            image = Image(portfolio=portfolio, title=portfolio.description[:200], image=request.FILES['image'])
            image.save()
            

            return redirect('my_portfolio')

    context = {'form': form}

    return render(request, template_name, context)


def portfolio_search(request):
    template_name = "includes/search.html"
    form = SearchForm()
    query = None
    results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
    
    if form.is_valid():
        query = form.cleaned_data['query']
        results = Portfolio.objects.annotate(
            search=SearchVector('title','description'), 
        ).filter(search=query)


    return render(request,template_name,{'form':form, 'query':query, 'results':results})

def upload_image(request):
    template_name = "includes/upload_image.html"
    
    portfolio = Portfolio.objects.filter(author=request.user)

    form = ImageLoadForm(request.user)
 
    context = {'form': form}

    if request.method == 'POST':
        user = request.user
        form = ImageLoadForm(request.user, request.POST, request.FILES)

        if form.is_valid():
            form.save()

    return render(request, template_name, context)

