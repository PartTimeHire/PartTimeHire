from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import JobRequest
from .forms import JobRequestForm, ProfileEditForm, SignUpForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib import messages

def home_view(request):
    if request.user.is_authenticated:
        print("User is authenticated")
        return render(request, 'home_authenticated.html')
    else:
        print("User is not authenticated")
        return render(request, 'home.html')

def home_authenticated(request):
    return render(request, 'home_authenticated.html')

def about(request):
    print("Rendering about page")
    return render(request, 'about.html')

@login_required
def create_job(request):
    if request.method == 'POST':
        print("Received POST request to create job")
        # Logic for handling form submission
        return HttpResponse("Job created successfully!")
    else:
        print("Rendering create job form")
        # Render the form for creating a job
        return render(request, 'create_job.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        print("Received POST request to edit profile")
        form = ProfileEditForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            print("Form is valid, saving profile changes")
            form.save()
            return redirect('home')
    else:
        print("Rendering edit profile form")
        form = ProfileEditForm(instance=request.user.userprofile)
    return render(request, 'edit_profile.html', {'form': form})

@login_required
def create_job_request(request):
    if request.user.is_authenticated:
        print("User is authenticated")
        if request.method == 'POST':
            print("Received POST request to create job request")
            form = JobRequestForm(request.POST)
            if form.is_valid():
                print("Form is valid, saving job request")
                form.save()
                return redirect('home')
        else:
            print("Rendering create job request form")
            form = JobRequestForm()
        return render(request, 'create_job_request.html', {'form': form})
    else:
        print("User is not authenticated")
        return redirect('redirect_to_signup_or_login')

@login_required
def job_search(request):
    print("Performing job search")
    job_requests = JobRequest.objects.all()
    return render(request, 'job_search.html', {'job_requests': job_requests})

def redirect_to_signup_or_login(request):
    print("Redirecting to signup or login page")
    return render(request, 'choose_signup_or_login.html')


def signup(request):
    if request.method == 'POST':
        print("Received POST request to signup view")
        form = SignUpForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            user = form.save(commit=False)
            user.is_active = False  # Deactivate user until email is verified
            user.save()
            verification_code = form.send_verification_email()  # Send verification email
            request.session['verification_code'] = verification_code  # Store verification code in session
            print("Verification code sent:", verification_code)  # Debugging print
            print("Email sent to:", form.cleaned_data['email'])  # Debugging print
            return redirect('email_verification')  # Redirect to verification page
        else:
            print("Form is invalid")
            print("Errors:", form.errors)  # Print form errors for debugging
            messages.error(request, 'Error processing your request. Please try again.')
    else:
        print("Received GET request to signup view")
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next', 'home_authenticated')
            return redirect(next_url)
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def user_logout(request):
    print("Logging out user")
    logout(request)
    return redirect('home')

@login_required
def verify_email(request):
    if request.method == 'POST':
        verification_code = request.POST.get('verification_code')
        stored_verification_code = request.session.get('verification_code')
        if verification_code == stored_verification_code:
            user = request.user
            user.is_active = True
            user.save()
            del request.session['verification_code']  # Remove verification code from session
            return redirect('home')
        else:
            return HttpResponse("Invalid verification code. Please try again.")
    else:
        return render(request, 'email_verification.html')
