from django.db import models
from django.contrib.auth.models import User

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=50, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Editora(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    ano_publicacao = models.PositiveIntegerField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.titulo


class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # aproveita o sistema de usuários do Django
    data_emprestimo = models.DateField(auto_now_add=True)
    data_devolucao = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.livro.titulo} emprestado para {self.usuario.username}"
