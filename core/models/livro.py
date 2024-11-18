from django.db import models
from uploader.models import Image
from .categoria import Categoria
from .editora import Editora
from .autor import Autor
from .tipo import Tipo
from django.core.validators import  MinValueValidator, MaxValueValidator


class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=32, blank=True, null=True)
    quantidade = models.IntegerField(default=0)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="livros", blank=True, null=True)
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT, related_name="livros", blank=True, null=True)
    autores = models.ManyToManyField(Autor, related_name="livros", blank=True)
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT, related_name="livros", blank=True, null=True)
    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    completo = models.BooleanField(default=False)

    def __str__(self):
        return f"({self.id}) {self.titulo} ({self.quantidade})"


class AvaliacaoLivro(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='avaliacoes')
    puntuacao = models.FloatField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comentario = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Avaliação de {self.livro.titulo} - {self.puntuacao} estrelas"
