from rest_framework.serializers import (
    ModelSerializer,
    SlugRelatedField,
    SerializerMethodField,
)
from uploader.models import Image
from uploader.serializers import ImageSerializer
from core.models import Manhwa, AvaliacaoMahhwa, Capitulo


class ManhwaSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa_url = SerializerMethodField()
    calificacion_prom = SerializerMethodField()
    numero_capitulos = SerializerMethodField()  # Novo campo: número de capítulos

    class Meta:
        model = Manhwa
        fields = ("id", "titulo", "tipo", "capa_url", "calificacion_prom", "numero_capitulos")

    def get_capa_url(self, obj):
        if obj.capa:
            return obj.capa.url
        return None

    def get_calificacion_prom(self, obj):
        avaliacoes = AvaliacaoMahhwa.objects.filter(manhwa=obj)
        if avaliacoes.exists():
            promedio = sum(avaliacao.puntuacao for avaliacao in avaliacoes) / avaliacoes.count()
            return round(promedio, 2)
        return None

    def get_numero_capitulos(self, obj):
        """
        Retorna o número de capítulos associados ao manhwa.
        """
        return obj.capitulos.count()


class ManhwaDetailSerializer(ModelSerializer):
    capa = ImageSerializer(required=False)
    calificacion_prom = SerializerMethodField()
    tipo = SerializerMethodField()
    numero_capitulos = SerializerMethodField()  # Número de capítulos

    class Meta:
        model = Manhwa
        fields = ("id", "titulo", "tipo", "capa", "calificacion_prom", "descricao", "numero_capitulos")
        depth = 1

    def get_calificacion_prom(self, obj):
        avaliacoes = AvaliacaoMahhwa.objects.filter(manhwa=obj)
        if avaliacoes.exists():
            promedio = sum(avaliacao.puntuacao for avaliacao in avaliacoes) / avaliacoes.count()
            return round(promedio, 2)
        return None

    def get_tipo(self, obj):
        return obj.tipo if obj.tipo else "Desconhecido"

    def get_numero_capitulos(self, obj):
        """
        Retorna o número de capítulos associados ao manhwa.
        """
        return obj.capitulos.count()


class ManhwaListSerializer(ModelSerializer):
    capa_url = SerializerMethodField()
    calificacion_prom = SerializerMethodField()
    numero_capitulos = SerializerMethodField()  # Novo campo: número de capítulos

    class Meta:
        model = Manhwa
        fields = ("id", "titulo", "tipo", "capa_url", "calificacion_prom", "numero_capitulos")

    def get_capa_url(self, obj):
        if obj.capa:
            return obj.capa.url
        return None

    def get_calificacion_prom(self, obj):
        avaliacoes = AvaliacaoMahhwa.objects.filter(manhwa=obj)
        if avaliacoes.exists():
            promedio = sum(avaliacao.puntuacao for avaliacao in avaliacoes) / avaliacoes.count()
            return round(promedio, 2)
        return None

    def get_numero_capitulos(self, obj):
        """
        Retorna o número de capítulos associados ao manhwa.
        """
        return obj.capitulos.count()
