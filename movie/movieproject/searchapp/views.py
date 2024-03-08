from django.shortcuts import render
from django.db.models import Q
from movieapp.models import Movie


# Create your views here.

# def SearchResult(request):
#     movies = None
#     query = None
#     if 'q' in request.GET:
#         query = request.GET.get('q')
#         movies = Movie.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
#         return render(request, 'search.html', {'query': query, 'movies': movies})


def searchBar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            movies = Movie.objects.filter(name__icontains=query)
            return render(request, 'searchbar.html', {'movies':movies})
        else:
            print("No information to show")
            return render(request, 'searchbar.html', {})

