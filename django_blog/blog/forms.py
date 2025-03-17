from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreatinoForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class ProfileForm(form.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]
    
    bio = forms.CharField(widget=forms.Textarea, required=False)
    profile_picture = forms.ImageField(required=False)

