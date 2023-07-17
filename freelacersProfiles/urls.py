from django.urls import path
from . import views

app_name = 'FreelanerGeorgia'

urlpatterns = [
    path('freelancers/', views.freelancer_list, name='freelancer_list'),
    path('freelancers/create/', views.freelancer_create, name='freelancer_create'),
]