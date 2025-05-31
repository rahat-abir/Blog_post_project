from django.urls import path
from .views import post_list, post_details

urlpatterns = [
    path("",post_list, name = 'post_list'),
    path("post/<int:id>",post_details, name = 'post_details'),
]
