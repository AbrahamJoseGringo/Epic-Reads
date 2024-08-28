from django.db import models

from uploader.models import Image

from .categoria import Categoria
from .tipo import Tipo


class Manhwa(models.Model):
    titulo = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="manhwas", blank=True, null=True)
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT, related_name="manhwas", blank=True, null=True)
    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return f"({self.id}) {self.titulo}"
