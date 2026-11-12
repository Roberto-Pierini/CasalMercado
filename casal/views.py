from django.shortcuts import render
from django.contrib.auth.models import User

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
    