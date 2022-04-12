from django.urls import path
from . import views

app_name = 'event'
urlpatterns = [
    path('', views.event_list, name='list'),
    path('<int:pk>/', views.event_detail, name='detail'),
    path('create/', views.event_create, name='create'),
]


