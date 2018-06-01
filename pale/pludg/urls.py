"""pludg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, re_path
from django.contrib import admin

from . import views

urlpatterns = [
    #url(r'projects/$', views.PludgProjectsView.as_view()),
    url(r'objects/$', views.PludgObjectsView.as_view()),
    re_path(r'object/(?P<objk>[0-9]+)/', views.PludgObjectView.as_view()),
    url(r'history/$', views.PludgHistoryView.as_view()),
    url(r'news/$', views.PludgNewsView.as_view()),
    url(r'news/article/$', views.PludgNewsArticleView.as_view()),
    url(r'impressum/$', views.PludgImpressumView.as_view()),
    url(r'contact/$', views.PludgContactView.as_view()),
    url(r'^$', views.PludgHomeView.as_view()),
]
