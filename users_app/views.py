from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy


def login_view(request):
    """Function to display login form. It allows authenticating user."""
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse_lazy('home_page_app:home_view'))
    else:
        form = AuthenticationForm()

    return render(request, 'users_app/login.html', context={'form': form})


def logout_view(request):
    """Function to display logout form. It allows deleting session for current user."""
    if request.method == 'POST':
        logout(request)
        return render(request, 'users_app/logged_out.html')
    user = request.user
    return render(request, 'users_app/logout.html', context={'user': user})
