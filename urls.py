# urls.py

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('about/', views.about, name='about'),
    path('create-job/', views.create_job, name='create_job'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('create-job-request/', views.create_job_request, name='create_job_request'),
    path('job-search/', views.job_search, name='job_search'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('choose-signup-or-login/', views.redirect_to_signup_or_login, name='choose_signup_or_login'),
    path('email-verification/', views.verify_email, name='email_verification'),  # Updated path
    path('home-authenticated/', views.home_authenticated, name='home_authenticated'),
    # Django Allauth URLs
    path('accounts/', include('allauth.urls')),
]
