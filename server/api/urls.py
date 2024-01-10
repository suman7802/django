from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_home),
    path('data/', views.api_body),
    path('params/', views.api_params),
    path('post/', views.api_form),
    path('get/<str:id>/', views.api_data_id),
    path('get/', views.api_data)
]