from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('fp/', views.fp, name='fp'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('bank/', views.bank, name='bank'),
    path('upload/', views.upload, name='upload'),
    path('upload2/', views.upload2, name='upload2'),
    path('<str:filepath>/', views.download_file)

]