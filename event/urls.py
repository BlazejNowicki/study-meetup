from django.urls import path
from . import views

app_name = 'event'
urlpatterns = [
    path('', views.event_list, name='list'),
    path('create/', views.event_create, name='create'),
]

