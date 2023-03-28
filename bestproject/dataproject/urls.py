from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('signup/', views.user_signup, name='user_signup'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('storage/', views.storage, name='storage'),
]
