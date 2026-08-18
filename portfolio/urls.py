from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('education/', views.education, name='education'),
]