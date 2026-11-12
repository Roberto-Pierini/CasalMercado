from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def cadastro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not User.objects.filter(username = username).exists():
            User.objects.create_user(username=username, email=email, password=password)
            return render(request, 'casal/cadastro.html',{'sucesso': 'Usuário cadastrado!'} )
        else:
             return render(request, 'casal/cadastro.html', {'erro': 'Este nome de usuário já está em uso.'})
    
    return render(request, 'casal/cadastro.html')

def logar(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('/casal/home/')
        else:
            return render(request, '/casal/login.html', {'erro': 'Usuário ou Senha inválido'})
    return render(request, 'casal/login.html')


def deslogar(request):
    logout(request)
    return redirect('/casal/login/')

@login_required(login_url='/casal/login/')
def home(request):
    return render(request, 'casal/home.html')

    