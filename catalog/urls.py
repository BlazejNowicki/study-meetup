from django.urls import path
from . import views

app_name = 'catalog'
urlpatterns = [
    path('', views.catalog_root, name='root'),
    path('course/', views.course_list, name='course_list'),
    path('disciplines/', views.discipline_list, name='discipline_list'),
    path('faculties/', views.faculties_list, name='faculties_list'),
    path('univiersities/', views.universities_list, name='universities_list')
]


