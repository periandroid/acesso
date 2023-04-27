from django.shortcuts import render, redirect
from .models import Perfil
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .models import TransporteEscolar

def index (request):
    return render (request, 'index.html');

def administrador (request):
    if request.user.is_staff:
        transporte_escolar_list = TransporteEscolar.objects.all()
        usuario_list = Perfil.objects.all()
        return render (request,'administrador.html', {'transporte_escolar_list': transporte_escolar_list, 'usuario_list': usuario_list},);
    else:
        return render('index')

def paginaInicial (request):
    if request.user.is_authenticated:
        return render (request, 'usuario.html');
    else:
        return render('index')

def deferir (request):
    return render (request, 'deferir.html');


def solicita_transporte (request):
    if request.user.is_authenticated:
        if request.POST:
            escola = request.POST['escola']
            endereco = request.POST['endereco']
            destino = request.POST['destino']
            turno = request.POST['turno']
            dia = request.POST['dia']
            status = request.POST['status']
            
            #Validações    
            if not escola.strip(): 
                messages.error(request, "Escola não informada, informe a escola")
                return redirect('solicita_transporte')
            if not endereco.strip():
                messages.error(request, "Endereço não informado, informe o endereço")
                return redirect('solicita_transporte')
            if not turno.strip():
                messages.error(request, "Turno não informada, informe o turno")
                return redirect('solicita_transporte')
            if not dia.strip():
                messages.error(request, "Dia não informado, informe o dia")
                return redirect('solicita_transporte')
            
            transporte = TransporteEscolar(escola = escola,  endereco = endereco,  destino = destino, turno = turno, dia = dia, status = status)
            transporte.save()
            messages.success(request,'Sua solicitação foi enviada com sucesso!')
            return redirect('paginaInicial')
        else:
            return render (request, 'transporte.html');
    else:
        return render('login')



def remover(request, id):
    if request.user.is_staff:
        transporte = TransporteEscolar.objects.get(pk=id)
        if transporte != None:
            transporte.delete()
            messages.success(request, "Solicitação removida com sucesso")    
        else:
            messages.error(request, "Solicitação não encontrado")
        
        return redirect('administrador');
    else:
        return render('login')

def editarstatus(request, id):
    transporte = TransporteEscolar.objects.get(pk=id)
    ctx = {
        'c': transporte
    }
    if request.POST:
        status = request.POST['status']

        transporte.status = status
        transporte.save()
        return redirect('administrador') 
    else:
        return render(request, "deferir.html", ctx)

def editarDados(request, id):
    usuario = Perfil.objects.get(pk=id)
    ctx = {
        'c': usuario
    }
    if request.POST:
        n = request.POST["nome"]
        c = request.POST["cpf"]
        e = request.POST["email"]

        usuario.nome = n
        usuario.cpf = c
        usuario.email = e
        usuario.save()
        return redirect('dashboard') 
    else:
        return render(request, "editar.html", ctx)
    
def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'dashboard.html',);
    else:
        return redirect('index')
    
def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        cpf = request.POST['cpf']
        email = request.POST['email']
        numero_casa = request.POST['numero_casa']
        rua = request.POST['rua']
        bairro = request.POST['bairro']
        complemento = request.POST['complemento']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        #Validações    
        if not nome.strip(): 
            print('O campo precisa ser preenchido')
            return redirect('cadastro')
        if not email.strip():
            print('O campo precisa ser preenchido')
            return redirect('cadastro')
        if not senha.strip():
            print('O campo precisa ser preenchido')
            return redirect('cadastro') 
        if not senha2.strip():
            print('O campo precisa ser preenchido')
            return redirect('cadastro')
        if senha != senha2:
            print('As senhas não são iguais.')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            print('Usuário já cadastrado')
            return redirect('cadastro')
        if type(numero_casa) != int:
            numero_casa = None
        user = User.objects.create_user(username=nome, email=email, password=senha)
        perfil = Perfil.objects.create(user=user,  cpf=cpf,  numero_casa=numero_casa, rua=rua, bairro=bairro, complemento=complemento )
        perfil.save()
        messages.success(request,'Usuário criado com sucesso!')
        return redirect('login')
    else:
        return render(request, 'cadastro.html')  
    
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        #Validações
        if not email.strip():
            messages.warning(request,'Preencha o campo do email')
            return redirect('login')
        if not senha.strip():
            messages.warning(request,'Preencha o campo da senha')
            return redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            #autenticação do django
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                messages.success(request,'Login realizado com sucesso')
                return redirect('dashboard')
            else:
                messages.error(request,'Senha incorreta')
            return redirect('login')
        else:
            messages.error(request,'Email incorreto')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

