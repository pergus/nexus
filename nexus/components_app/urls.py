from django.urls import path
from . import views

app_name = 'components_app'

urlpatterns = [
    path('all-components-demo/', views.all_components_demo, name='all-components-demo'),
]
