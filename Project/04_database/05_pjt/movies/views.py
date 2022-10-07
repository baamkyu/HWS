from django.shortcuts import render, redirect
from movies.models import Movie
from movies.forms import MovieForm

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)

def create(request):
    if request.method == 'POST':
        movieform = MovieForm(request.POST)
        if movieform.is_valid():
            movie = movieform.save()
            return redirect('movies:detail', movie.pk)
    else:
        movieform = MovieForm()
    context = {
        'movieform': movieform,
    }
    return render(request, 'movies/create.html', context)

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)  # 특정 레코드를 가져온 후에
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)  # 바로 context 인자로 넣어줌


def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        movieform = MovieForm(request.POST, instance=movie)
        if movieform.is_valid():
            movieform.save()
            return redirect('movies:detail', movie.pk)
    else:
        movieform = MovieForm(instance=movie)
    context = {
        'movie': movie,
        'movieform': movieform
    }
    return render(request, 'movies/update.html', context)

def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')