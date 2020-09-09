from django.urls import path
from . import views

app_name = "homes"
urlpatterns = [
    path("", views.base, name='base'),
]