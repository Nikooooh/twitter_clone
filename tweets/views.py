from django.shortcuts import render, redirect
from .forms import RegistrationForm, TweetForm, CustomRegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Tweet
import logging

logger = logging.getLogger(__name__)

def register(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print("Usuário autenticado:", user.username)  
                login(request, user)
                logger.info(f"Usuário {username} autenticado com sucesso.")
                messages.success(request, 'Parabéns, usuário autenticado!')
                return redirect('congratulations')
            else:
                print("Usuário não autenticado")  
                logger.warning(f"Tentativa de login com usuário {username} falhou.")
                messages.error(request, 'Por favor, digite um nome de usuário e senha corretos.')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def index(request):
    return render(request, 'index.html')

def congratulations(request):
    tweets = Tweet.objects.all()
    form = TweetForm()

    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            new_tweet = form.save(commit=False)
            new_tweet.user = request.user
            new_tweet.save()
            form = TweetForm()

    return render(request, 'congratulations.html', {'tweets': tweets, 'form': form})
