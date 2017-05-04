from django.conf.urls import include, url
from django.contrib import admin
urlpatterns = [
    url(r'^citdjango/', include('citdjango.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^webapp/', include('webapp.urls')),
    url(r'^spotify/', include('Spotify.urls')),
    url(r'^', include('personal.urls')),
]