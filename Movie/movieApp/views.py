from django.shortcuts import render
from .forms import MovieForm
from .models import Movie


def index(request):
    return render(request, 'movieApp/index.html')


def listMovies(request):
    movies = Movie.objects.all()
    return render(request, 'movieApp/listMovies.html', {'movies': movies})


def addMovie(request):
    form = MovieForm()
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    return render(request, 'movieApp/addMovie.html', {'form': form})
