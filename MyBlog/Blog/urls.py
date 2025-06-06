from django.urls import path
from .views import post_list, post_details, signup_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",post_list, name = 'post_list'),
    path("post/<int:id>",post_details, name = 'post_details'),
    path("login/", auth_views.LoginView.as_view(template_name = "registration/login.html"), name = "login"),
    path("logout/", auth_views.LogoutView.as_view(), name = "logout"),
    path("signup/", signup_view, name = "signup"),
]
