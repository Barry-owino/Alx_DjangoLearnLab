from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, ProfileForm

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if forms.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form':form})

@login_required
def profile_view(request):
    if request.method == 'POST':
        user_form = ProfileForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST,request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.isvalid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = ProfileForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'blog/profile.html', {'form': form, 'profile_form': profile_form})
