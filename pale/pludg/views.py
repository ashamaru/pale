# from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.core.mail import send_mail

import datetime

from . import forms

# Create your views here.

from .models import NewsArticle, Object, ObjectImage

class PludgHomeView(generic.TemplateView):
    template_name = 'pludg/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = NewsArticle.objects.all()
        return context


class PludgObjectsView(generic.TemplateView):
    template_name = 'pludg/references.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        raw_objs = Object.objects.all()
        objects = [ ]
        for obj in raw_objs:
            object = { }
            object['object']= obj
            thumb = ObjectImage.objects.all().filter(object__name=obj.name).filter(category='thumbnail')
            if thumb.count() > 0:
                object['thumbnail'] = thumb[0]
            #else:
             #   object['thumbnail'] = default
            objects.append(object)
        context['objects'] = objects
        return context



class PludgObjectView(generic.TemplateView):
    template_name = 'pludg/reference.html'
    objk = None

    def get(self, request, *args, **kwargs):
        self.objk = kwargs['objk']
        return super(PludgObjectView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        objk = Object.objects.get(pk=self.objk)
        context['reference'] = objk
        images = { }
        images['main'] = ObjectImage.objects.get(category='main')
        maps = ObjectImage.objects.all().filter(object=objk).filter(category='map')
        if maps.count() > 0:
            images['map'] = maps[0]
        #else:
            #images['mao'] = 'standard image'
        gallery = ObjectImage.objects.all().filter(object=objk).filter(category='gallery')
        images['gallery'] = gallery
        context['images'] = images
        return context



class PludgHistoryView(generic.TemplateView):
    template_name = 'pludg/history.html'

class PludgNewsView(generic.TemplateView):
    template_name = 'pludg/news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = NewsArticle.objects.all().exclude(start_tp__gte=datetime.datetime.now()).exclude(end_tp__lte=datetime.datetime.now())
        return context

class PludgNewsArticleView(generic.TemplateView):
    template_name = 'pludg/news_article.html'

class PludgImpressumView(generic.TemplateView):
    template_name = 'pludg/impressum.html'


class PludgContactView(generic.TemplateView):
    template_name = 'pludg/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.ContactForm()
        return context

    def post(self, request, *args, **kwargs):
        PludgContactView.handleMailRequest(request)
        return HttpResponse('U sended the contact form .. congrats ^^')

    @staticmethod
    def handleMailRequest(request):
        first_name = request.POST['first_name']
        name = request.POST['name']
        # business = request.POST['business']
        plz_city = request.POST['plz_city']
        street = request.POST['street']
        country = request.POST['country']
        phone = request.POST['phone']
        sender = request.POST['sender']
        subject = request.POST['subject']
        message = request.POST['message']
        # cc_myself = request.POST['cc_myself']
        genmsg = 'Kontakt\nName: ' + name + ' ' + first_name + '\nStraße: ' + street + '\n'
        genmsg += 'Stadt: ' + plz_city + '\nNummer: ' + phone + '\n'
        genmsg += 'Email: ' + sender + '\n\n'
        genmsg += message
        return send_mail(subject, genmsg, 'tomh2d@web.de', ['thomas1.hildebrand@st.oth-regensburg.de'], False)

