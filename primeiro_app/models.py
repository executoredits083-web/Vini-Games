from django.db import models


class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Perfil(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    foto = models.ImageField(upload_to='fotos_perfil/', null=True, blank=True)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome