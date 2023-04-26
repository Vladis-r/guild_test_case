import os
import requests

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv

load_dotenv()


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            error_message = "Неверные данные. Попробуйте ещё раз."
    else:
        error_message = None
    return redirect(request, 'login.html', {'error_message': error_message})


@csrf_exempt
def logout_view(request):
    logout(request)
    return render(request, 'login.html', {'error_message': "Вы вышли из системы."})


@csrf_exempt
def kinopoisk_view(request):
    url = "https://api.kinopoisk.dev/v1/movie?selectFields=id%20name%20rating.kp%20description%20poster.previewUrl%20genres.name%20countries.name&sortField=rating.kp&sortType=-1&page=1&limit=5"

    headers = {
        "X-API-KEY": os.getenv("KINOPOISK_API")
    }

    if request.method == "GET":
        response = requests.get(url, headers=headers)
        data = response.json()
        context = {
            'movies': data['docs']
        }
        return render(request, 'top_movies.html', context)
