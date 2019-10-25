from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='to_do_list-home'),
    path('about/', views.about, name='to_do_list-about'),
]