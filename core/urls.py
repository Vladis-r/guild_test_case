from django.urls import path
from core import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('top_movies/', views.kinopoisk_view, name='kinopoisk'),
]
