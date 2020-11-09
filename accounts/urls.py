from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns =[
    path('', views.login, name='index_login'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('dashboard/',  csrf_exempt(views.dashboard), name='dashboard'),
]