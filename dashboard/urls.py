from django.contrib import admin
from django.urls import path

from .import views
app_name = "dashboard"

urlpatterns = [
    path('', views.homepage, name='homepage'),

    path('form/', views.booking, name='booking'),
    path('details/', views.details, name='details'),
    # path('bk_form/', views.bk_form, name='bk_form'),

]
