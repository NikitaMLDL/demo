from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('', partners_list, name='partners_list'),
    path('add/', add_partner, name='add_partner'),
    path('<int:partnerid>/edit/', edit_partner, name='edit_partner'),
    path('<int:partnerid>/history/', history_partner, name='history_partner')
]