from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect
from django.shortcuts import render


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('shop:product_list')  # Перенаправлення на сторінку панелі керування після входу
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('accounts:login')  # Перенаправлення на сторінку входу


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Автоматичний вхід після реєстрації
            login(request, user)
            return redirect('shop:product_list')  # Перенаправлення на сторінку панелі керування після реєстрації
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})



