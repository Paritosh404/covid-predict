from django.urls import path
from . import views
urlpatterns =[

    path('home',views.index,name='index'),
    path('admin$',views.adm,name='adm'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('',views.register,name='register'),
    path('update',views.update,name='update'),
    path('results',views.result,name='result')


]

