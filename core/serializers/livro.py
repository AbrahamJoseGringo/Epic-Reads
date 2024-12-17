from rest_framework import serializers
from rest_framework.serializers import (
    DecimalField,
    ModelSerializer,
    Serializer,
    SlugRelatedField,
    ValidationError,
    SerializerMethodField,
)
from uploader.models import Image
from uploader.serializers import ImageSerializer
from core.models import Livro, AvaliacaoLivro


# Serializer de Detalhes do Livro (com autores)
class LivroDetailSerializer(ModelSerializer):
    completo = SerializerMethodField()
    calificacion_promedio = SerializerMethodField()
    capa_url = SerializerMethodField()
    autores = SerializerMethodField()  # Lista de autores

    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1

    def get_completo(self, obj):
        return obj.completo

    def get_calificacion_promedio(self, obj):
        avaliacoes = obj.avaliacoes.all()  # Acessa avaliações pelo related_name
        if avaliacoes.exists():
            promedio = sum(avaliacao.puntuacao for avaliacao in avaliacoes) / avaliacoes.count()
            return round(promedio, 2)
        return None

    def get_capa_url(self, obj):
        if obj.capa:
            return obj.capa.url
        return None

    def get_autores(self, obj):
        # Retorna uma lista dos nomes dos autores
        return [autor.nome for autor in obj.autores.all()] or "Autor desconhecido"


# Serializer para a Listagem de Livros
class LivroListSerializer(ModelSerializer):
    completo = SerializerMethodField()
    calificacion_promedio = SerializerMethodField()
    capa_url = SerializerMethodField()
    autores = SerializerMethodField()

    class Meta:
        model = Livro
        fields = ("id", "titulo", "preco", "completo", "calificacion_promedio", "capa_url", "autores")

    def get_completo(self, obj):
        return obj.completo

    def get_calificacion_promedio(self, obj):
        avaliacoes = obj.avaliacoes.all()
        if avaliacoes.exists():
            promedio = sum(avaliacao.puntuacao for avaliacao in avaliacoes) / avaliacoes.count()
            return round(promedio, 2)
        return None

    def get_capa_url(self, obj):
        if obj.capa:
            return obj.capa.url
        return None

    def get_autores(self, obj):
        # Retorna uma lista dos nomes dos autores
        return [autor.nome for autor in obj.autores.all()] or "Autor desconhecido"


# Serializer Principal para Livro
class LivroSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    completo = SerializerMethodField()
    calificacion_promedio = SerializerMethodField()
    capa_url = SerializerMethodField()
    autores = SerializerMethodField()

    class Meta:
        model = Livro
        fields = "__all__"

    def get_completo(self, obj):
        return obj.completo

    def get_calificacion_promedio(self, obj):
        avaliacoes = obj.avaliacoes.all()
        if avaliacoes.exists():
            promedio = sum(avaliacao.puntuacao for avaliacao in avaliacoes) / avaliacoes.count()
            return round(promedio, 2)
        return None

    def get_capa_url(self, obj):
        if obj.capa:
            return obj.capa.url
        return None

    def get_autores(self, obj):
        # Retorna uma lista dos nomes dos autores
        return [autor.nome for autor in obj.autores.all()] or "Autor desconhecido"
