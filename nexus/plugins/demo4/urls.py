from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="demo4_index"),
]
