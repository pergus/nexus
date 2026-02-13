from django.urls import path
from . import views

app_name = 'components_app'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('all-components-demo/', views.all_components_demo, name='all-components-demo'),
    path('sidebar-demo/', views.sidebar_demo, name='sidebar-demo'),
    path('maps/google/', views.google_maps_demo, name='google-maps'),
    path('maps/vector/', views.vector_maps_demo, name='vector-maps'),
    path('charts/', views.charts_demo, name='charts'),
    path('tables/basic/', views.basic_tables_demo, name='basic-tables'),
    path('tables/data/', views.data_tables_demo, name='data-tables'),
    path('forms/basic/', views.basic_forms_demo, name='basic-forms'),
    path('forms/advanced/', views.advanced_forms_demo, name='advanced-forms'),
    path('forms/validation/', views.validation_forms_demo, name='validation-forms'),
]
