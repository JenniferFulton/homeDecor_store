from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('new_item', views.new_item),
    path('new_warehouse', views.new_warehouse),
]