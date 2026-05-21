from django.db import models


class Serviço(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_length==10)
    ativo = models.BooleanField(default=True)

    def _str_(self):
        return self.nome
# Create your models here.

class Perfil(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailFeld()
    foto = models.ImageField(upload_to='fotos_oerfil/', null=True)
    telefone = models.CharField(max_length=20)

    _str_(nome):
    return