from django.conf.urls import url
from . import views
from django.views.generic import DetailView, ListView
from personal.models import Post

urlpatterns = [
    url(r'^', views.index, name='index'),
    url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25], template_name="personal/posts.html")),

]

