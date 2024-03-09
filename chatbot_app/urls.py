from django.urls import path

from . import views

urlpatterns = [
    path("", views.ChatBot_index, name="ChatBot_index"),
]