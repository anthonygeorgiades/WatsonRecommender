from django.conf.urls import include, url
from django.contrib import admin
urlpatterns = [
    url(r'^citdjango/', include('citdjango.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^webapp/', include('webapp.urls')),
    url(r'^Spotify/', include('Spotify.urls')),
    url(r'^$', include('personal.urls')),
    url(r'^watson_app/', include('watson_app.urls')),

]