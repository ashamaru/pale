# from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

# Create your views here.


class PludgHomeView(generic.TemplateView):
    template_name = 'pludg/home.html'


class PludgImpressumView(generic.TemplateView):
    template_name = 'pludg/impressum.html'
