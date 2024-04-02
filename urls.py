from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # URL pattern for the home page
    path('about/', views.about, name='about'),  # URL pattern for the about page
    path('create_job/', views.create_job, name='create_job'),  # URL pattern for creating a job
    path('edit_profile/', views.edit_profile, name='edit_profile'),  # URL pattern for editing a profile
    # Add more URL patterns for other views as needed
]
