from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('', views.user_home, name='root'),
    path('signin/', views.user_signin, name='signin'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
]


