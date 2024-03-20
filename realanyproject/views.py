from django.shortcuts import render
from .models import Movie, Music, Book

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})

def music_list(request):
    music = Music.objects.all()
    return render(request, 'music_list.html', {'music': music})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import render, redirect

from realanyproject.models import CategoryModel, Music, Movie, Book
# from .forms import SearchForm


def home_page(request):
    categories = CategoryModel.objects.all()
    music = Music.objects.all()
    movie = Movie.objects.all()
    book = Book.objects.all()
    form = SearchForm
    context = {'categories': categories, 'music': music, 'movie': movie, 'book': book ,'form': form}
    return render(request, template_name='index.html', context=context)


class MyLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return '/'


def logout_view(request):
    logout(request)
    return redirect('home')


def search(request):
    if request.method == "POST":
        get_song = request.POST.get('search_song')
        try:
            exact_song = Music.objects.get(pr_name__icontains=get_song)
            return redirect(f'/music/{exact_song.id}')
        except:
            return redirect('/')
    elif request.method == "POST":
        get_movie = request.POST.get('search_movie')
        try:
            exact_movie = Music.objects.get(pr_name__icontains=get_movie)
            return redirect(f'/movie/{exact_movie.id}')
        except:
            return redirect('/')
    elif request.method == "POST":
        get_book = request.POST.get('search_book')
        try:
            exact_book = Music.objects.get(pr_name__icontains=get_book)
            return redirect(f'/book/{exact_book.id}')
        except:
            return redirect('/')

def music_page(request, pk):
    song = Music.objects.get(id=pk)
    context = {'song': song }
    return render(request, 'music.html', context)

def movie_page(request, pk):
    movie = Movie.objects.get(id=pk)
    context = {'movie': movie }
    return render(request, 'movie.html', context)

def book_page(request, pk):
    book = Book.objects.get(id=pk)
    context = {'book': book }
    return render(request, 'book.html', context)

def category_page(request, pk):
    category = CategoryModel.objects.get(id=pk)
    current_songs = Music.objects.filter(music_category=category)
    context = {'music': current_songs}
    return render(request, 'music.html', context)
    current_movies = Movie.objects.filter(movie_category=category)
    context = {'movie': current_movies}
    return render(request, 'movie.html', context)
    current_book = Book.objects.filter(book_category=category)
    context = {'book': current_book}
    return render(request, 'book.html', context)

def category_page(request, pk):
    category = CategoryModel.objects.get(id=pk)
    current_songs = Music.objects.filter(music_category=category)
    context = {'music': current_songs}
    return render(request, 'music.html', context)
    current_movies = Movie.objects.filter(movie_category=category)
    context = {'movie': current_movies}
    return render(request, 'movie.html', context)
    current_book = Book.objects.filter(book_category=category)
    context = {'book': current_book}
    return render(request, 'book.html', context)
    return render(request, 'category.html', context)