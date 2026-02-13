from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="demo2_index"),
]
