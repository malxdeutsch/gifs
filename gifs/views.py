from django.shortcuts import render
from .models import Gif_Model, Category

# Create your views here.
def homepage(request):
    all_gifs = Gif_Model.objects.all()
    return render(request, 'homepage.html',{'all_gifs':all_gifs})

def category(request, category_id):
    category = Category.objects.get(id = category_id)
    each_gif = category.gifs.all()
    return render(request, 'category.html', {'category':category, 'each_gif':each_gif})

def categories(request):
    all_categories = Category.objects.all()
    return render(request, 'categories.html',{'all_categories':all_categories})

def gif(request, gif_id):
    gif = Gif_Model.objects.get(id = gif_id)
    return render (request, 'gif.html', {'gif':gif} )