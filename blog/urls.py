from django.urls import path
from .views import post , post_create, home , feedback_list
urlpatterns = [
    path('',home,name='home'),
    path('post1', post, name='post'),
    path('post', post_create, name='post_create'),
    path('feedback', feedback_list, name='feedback_list'),

]