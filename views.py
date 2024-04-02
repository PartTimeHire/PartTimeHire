from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def create_job(request):
    if request.method == 'POST':
        # Logic for handling form submission
        return HttpResponse("Job created successfully!")  # Example response
    else:
        # Render the form for creating a job
        return render(request, 'create_job.html')

def edit_profile(request):
    if request.method == 'POST':
        # Logic for handling profile editing
        return HttpResponse("Profile edited successfully!")  # Example response
    else:
        # Render the form for editing profile
        return render(request, 'edit_profile.html')

# Add more view functions as needed
