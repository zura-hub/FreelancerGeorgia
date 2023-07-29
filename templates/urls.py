

from django.urls import path
from . import views


urlpatterns = [
    path('', views.templates, name='templates'),
    path('create_template', views.create_template, name='create_template')
]
