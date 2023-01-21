from django.shortcuts import render
from .models import Movie
from django.http import Http404
# Create your views here.
def movie(request, movie_id):
   movie = Movie.objects.get(pk=movie_id)
   if movie is not None:
      return render (request,"movie.html",{"movie": movie})
   else:
      raise Http404("Movie doesn't exist")  