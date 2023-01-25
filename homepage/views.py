"""
views
"""


# from django.shortcuts import render
from django.views.generic import TemplateView
# from django.http import HttpResponse


# Create your views here.


class HomePageView(TemplateView):
    """
    Home page view
    """
    template_name = "home.html"


class AboutPageView(TemplateView):
    """
    Home page view
    """
    template_name = "about.html"
