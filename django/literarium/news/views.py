from django.shortcuts import render
from .models import NewsItem

def news_list(request):
    items = NewsItem.objects.all()
    return render(request, 'news/news_list.html', {'news': items})

