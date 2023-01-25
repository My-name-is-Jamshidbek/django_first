"""
views
"""
from django.shortcuts import render
from django.views.generic import ListView
from .models import New

# Create your views here.


class NewsListView(ListView):
    """
    news list view
    """
    model = New
    template_name = "news.html"
