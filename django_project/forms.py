from django import forms
from .models import UserProfile, Job, Rating, Category

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'bio', 'location']

class JobForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Job
        fields = ['title', 'description', 'amount', 'categories', 'deadline']

class JobProgressForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['progress']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']