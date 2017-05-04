from django.shortcuts import render
from .models import Post
import Spotify.spotifyquery


# Create your views here.
def index(request):
    return render(request, 'personal/home.html')