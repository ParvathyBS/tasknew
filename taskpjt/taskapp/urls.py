from django.urls import path
from . import views

app_name = 'taskapp'

urlpatterns = [
    path('', views.home, name="home"),
    path('taskapp/login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('<slug:c_slug>/', views.allBranch, name='branch_by_category'),
    path('register/forms', views.formfill, name='formfill'),
    path('<slug:c_slug>/<slug:sub_slug>/', views.subbranch, name='sub'),
    path('register/taskapp/login', views.login, name='login'),
    path('register/forms/print', views.printform, name='printform'),
]
