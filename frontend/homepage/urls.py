from django.urls import path
from homepage import views

urlpatterns = [
    path("", views.home, name="home"),
    path("index", views.index, name="index"),
    path("test", views.test, name="test"),
]