from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    error_message = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Nom d'utilisateur ou mot de passe incorrect."

    return render(request, 'accounts/login.html', {'error_message': error_message})


def logout_view(request):
    logout(request)
    return redirect('login')