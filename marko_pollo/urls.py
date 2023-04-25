from django.urls import path

from marko_pollo import views

urlpatterns = [
    path("one/", views.one_mp_view, name="one_mp"),
    path("list/", views.list_mp_view, name="list_mp"),
    path("range/", views.range_mp_view, name="range_mp"),
    # path("ws/", views.websocket_view, name="websocket"),
]
