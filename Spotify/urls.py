from django.conf.urls import url
from . import views
from django.views.generic import DetailView, ListView

urlpatterns = [
url(r'^', views.something, name='searchlanding'),
    url(r'^', views.index, name='index'),

]