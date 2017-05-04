from django.conf.urls import url
from . import views # "." is a relative import i.e. saying lets import from relative package

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

