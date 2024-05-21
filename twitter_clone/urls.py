from django.urls import path, include
from django.contrib import admin
from tweets import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tweets.urls')),
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),  
    path('congratulations/', views.congratulations, name='congratulations'),
]
