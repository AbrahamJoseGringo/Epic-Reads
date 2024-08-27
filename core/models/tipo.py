from django.db import models


class Tipo(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f"({self.id}) {self.descricao}"
