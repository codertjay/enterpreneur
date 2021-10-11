from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileUpdateForm, UserUpdateForm
from .models import Profile


def user_register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login!')
            return redirect('codertjay:home_page')
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})


def profile_view(request):
    u_form = UserUpdateForm(instance=request.user, )
    p_form = ProfileUpdateForm(request.FILES, instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            username = u_form.cleaned_data.get('username')
            email = u_form.cleaned_data.get('email')
            u_form.save()
            p_form.save()
            return redirect('users:profile')

    return render(request, 'users/profile.html', context)
