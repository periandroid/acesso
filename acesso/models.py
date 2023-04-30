from django.db import models
from django.contrib.auth.models import User

class TransporteEscolar(models.Model):
    nome = models.TextField(max_length=50, default="")
    escola = models.TextField(max_length=50, default="")
    endereco = models.TextField(max_length=50)
    destino = models.TextField(max_length=50)
    turno = models.TextField(max_length=20)
    dia = models.TextField(max_length=30)
    status = models.TextField(max_length=10, default="Análise")

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')    
    cpf = models.CharField(max_length=14)
    numero_casa = models.IntegerField(null=True)
    rua = models.TextField(max_length=25, null=True)
    bairro = models.TextField(max_length=20, null=True)
    complemento = models.TextField(max_length=25, null=True)
