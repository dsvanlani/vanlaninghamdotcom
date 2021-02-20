from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
import VanLaninghamDotCom.settings


urlpatterns = [
    path('login/',
         auth_views.LoginView.as_view(
             template_name='registration/login.html'),
            name='login'),
    path('logout', views.logout_request, name='logout')
]