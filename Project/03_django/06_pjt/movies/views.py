from django.shortcuts import render, redirect
<<<<<<< HEAD
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
=======
from .models import Movie

# Create your views here.
def index(request):
  movies = Movie.objects.all()
  context = {
    'movies':movies,
  }
  return render(request, 'movies/index.html', context)

def new(request):
  return render(request, 'movies/new.html')

def create(request):
  title = request.POST.get('title')
  audience = request.POST.get('audience')
  release_data = request.POST.get('release_data')
  genre = request.POST.get('genre')
  score = request.POST.get('score')
  poster_url = request.POST.get('poster_url')
  description = request.POST.get('description')
  movie = Movie(title=title, audience=audience, release_data=release_data, genre=genre, score=score, poster_url=poster_url, description=description)
  movie.save()
  return redirect('movies:index')

def detail(request, pk):
  movie = Movie.objects.get(pk=pk)
  context = {
    'movie':movie,
  }
  return render(request, 'movies/detail.html', context)

def delete(request, pk):
  movie = Movie.objects.get(pk=pk)
  movie.delete()
  return render(request, 'movies/index.html')

def edit(request, pk):
  movie = Movie.objects.get(pk=pk)
  context = {
    'movie':movie,
  }
  return render(request, 'movies/edit.html', context)

def update(request, pk):
  movie = Movie.objects.get(pk=pk)
  movie.title = request.POST.get('title')
  movie.audience = request.POST.get('audience')
  movie.release_data = request.POST.get('release_data')
  movie.genre = request.POST.get('genre')
  movie.score = request.POST.get('score')
  movie.poster_url = request.POST.get('poster_url')
  movie.description = request.POST.get('description')
  movie.save()
  return redirect('movies:detail', movie.pk)

>>>>>>> d91e101d9b9fccd0ec02132f6b839b5d2dcb06bf
