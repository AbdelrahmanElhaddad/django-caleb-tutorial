from django.http import HttpResponse
from django.shortcuts import render

data = { 'movies': [
    {
        'id': 0,
        'name': "Arcane",
        'year': 2021
    },
    {
        'id': 1,
        'name': "Horimiya",
        'year': 2021
    },
    {
        'id': 2,
        'name': "Orange",
        'year': 2021
    }
    ]}
    


def movies(request):
    return render(request, 'movies/movies.html', data)

def home(request):
    return HttpResponse("Home Page")