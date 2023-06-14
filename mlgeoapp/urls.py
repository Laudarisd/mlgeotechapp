from django.urls import path
from . import views
from . import login_reg_logout



urlpatterns = [
    path('', views.homeView, name='root'),  # Add this line for the root path
    path('nav/', views.navBar, name='nav'),
    path('home/', views.homeView, name='homeview'),

    #path('', login_reg_logout.login, name='login'),
    #path('', login_reg_logout.register, name='register'),
    #path('', login_reg_logout.logout, name='logout'),

]