from django.db import models
from uploader.models import Image, Document
from .categoria import Categoria
from .tipo import Tipo
from django.core.validators import MinValueValidator, MaxValueValidator


LANGUAGE_CHOICES = [
    ('PT', 'Português'),
    ('EN', 'Inglês'),
    ('ES', 'Espanhol'),
    ('JP', 'Japonês'),
]

class Manhwa(models.Model):
    numero = models.IntegerField(unique=True)  # Adicione unique=True se cada Manhwa tiver um número único
    titulo = models.CharField(max_length=255, blank=True, null=True)
    idioma = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default='PT')  # Define choices para idioma

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="manhwas",
        blank=True,
        null=True
    )

    tipo = models.ForeignKey(
        Tipo,
        on_delete=models.PROTECT,
        related_name="manhwas",
        blank=True,
        null=True
    )

    capa = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    documento = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
        related_name="capitulos",
        null=True,
        blank=True,
    )

    data_publicacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"({self.id}) {self.titulo or 'Sem título'} - Capítulo {self.numero}"

    class Meta:
        ordering = ['numero']  
        unique_together = ('numero', 'titulo') 

class AvaliacaoMahhwa(models.Model):
    manhwa = models.ForeignKey(Manhwa, on_delete=models.CASCADE, related_name='avaliacoes')
    puntuacao = models.FloatField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    comentario = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Avaliação de {self.manhwa.titulo} - {self.puntuacao} estrelas"

class Capitulo(models.Model):
    manhwa = models.ForeignKey(Manhwa, on_delete=models.CASCADE, related_name="capitulos")
    titulo = models.CharField(max_length=255)
    numero = models.IntegerField()

    def __str__(self):
        return f"Capítulo {self.numero}: {self.titulo}"
