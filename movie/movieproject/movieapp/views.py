from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import MovieForm
from movieapp.models import Category, Movie, Review
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.db.models import Q


# Create your views here.
def allProCat(request, c_slug=None):
    c_page = None
    movies_list = None
    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        movies_list = Movie.objects.all().filter(category=c_page)
    else:
        movies_list = Movie.objects.all().filter()
    paginator = Paginator(movies_list, 8)
    try:
        page = int(request.GET.get('page', 1))
    except:
        page = 1
    try:
        movies = paginator.page(page)
    except (EmptyPage, InvalidPage):
        movies = paginator.page(paginator.num_pages)

    return render(request, "category.html", {'category': c_page, 'movies': movies})


def add_movie(request):
    cat = Category.objects.all()
    user = request.user
    user_id=user.id
    # print(user_id)

    if request.method == 'POST':
        move_name = request.POST['move_name']
        slug = request.POST['move_name']
        slug = slug.replace(' ', '')
        poster = request.FILES['poster']
        description = request.POST['description']
        release_date = request.POST['release_date']
        actors = request.POST['actors']
        obj = request.POST['mcategory']
        var = Category.objects.get(id=obj)
        youtube_link = request.POST['youtube_link']
        movie = Movie(user_id=user_id,name=move_name, slug=slug, poster=poster, description=description, release_date=release_date,
                      actors=actors,
                      category=var, youtube_link=youtube_link)
        movie.save()
        return redirect('/')
    return render(request, "add_movie.html", {'cat': cat})


def proDetail(request, c_slug, movie_slug):
    user = request.user
    username_id = user.id

    try:
        movie = Movie.objects.get(category__slug=c_slug, slug=movie_slug)
    except Exception as e:
        raise e

    if request.method == 'POST':
        star_rating = request.POST.get('rating')
        item_review = request.POST.get('item_review')

        item_reviews = Review(username_id=username_id,movie=movie, rating=star_rating, review_desp=item_review)
        item_reviews.save()
    reviews = Review.objects.filter(movie=movie)
    return render(request, 'movie.html', {'movie': movie, 'reviews': reviews})


def update(request, id):
    movie = Movie.objects.get(id=id)
    # movie = get_object_or_404(Movie, id=id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, "movie_edit.html", {'form': form, 'movie': movie})


def delete(request, id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, "delete.html")


def SearchResult(request):
    movies = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        movies = Movie.objects.filter(name__icontains= query)
        # movies = Movie.objects.filter(Q(name__contains=query) | Q(category__contains=query))
        return render(request, 'search.html', {'query': query, 'movies': movies})


