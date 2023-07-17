from django.urls import path
from . import views


urlpatterns = [
    path('jobs', views.jobs, name='jobs'),
    path('create', views.create, name='create'),
    path('search', views.search, name='search'),
    path('<int:pk>', views.JobsDetailView.as_view(), name='detail'),
]
