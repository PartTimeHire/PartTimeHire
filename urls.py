from django.urls import path
from . import views

urlpatterns = [
    path('create-job/', views.create_job, name='create_job'),
    path('edit-job/<int:job_id>/', views.edit_job, name='edit_job'),
    # Add other URL patterns here
]
