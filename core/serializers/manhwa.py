from rest_framework.serializers import (
    ModelSerializer,
    SlugRelatedField,
    SerializerMethodField,
)
from uploader.models import Image
from uploader.serializers import ImageSerializer
from core.models import Manhwa, AvaliacaoMahhwa


class ManhwaSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa_url = SerializerMethodField()  # URL da capa
    calificacion_prom = SerializerMethodField()  # Média de avaliações

    class Meta:
        model = Manhwa
        fields = ("id", "titulo", "tipo", "capa_url", "calificacion_prom")

    def get_capa_url(self, obj):
        """
        Retorna a URL da capa se existir.
        """
        if obj.capa:
            return obj.capa.url
        return None

    def get_calificacion_prom(self, obj):
        """
        Retorna a média de avaliações do manhwa.
        """
        avaliacoes = AvaliacaoMahhwa.objects.filter(manhwa=obj)
        if avaliacoes.exists():
            promedio = sum(avaliacao.puntuacao for avaliacao in avaliacoes) / avaliacoes.count()
            return round(promedio, 2)
        return None


class ManhwaDetailSerializer(ModelSerializer):
    capa = ImageSerializer(required=False)
    calificacion_prom = SerializerMethodField()  # Média de avaliações
    tipo = SerializerMethodField()  # Inclui o campo 'tipo'

    class Meta:
        model = Manhwa
        fields = ("id", "titulo", "tipo", "capa", "calificacion_prom", "descricao")
        depth = 1

    def get_calificacion_prom(self, obj):
        """
        Retorna a média de avaliações do manhwa.
        """
        avaliacoes = AvaliacaoMahhwa.objects.filter(manhwa=obj)
        if avaliacoes.exists():
            promedio = sum(avaliacao.puntuacao for avaliacao in avaliacoes) / avaliacoes.count()
            return round(promedio, 2)
        return None

    def get_tipo(self, obj):
        """
        Retorna o tipo do manhwa.
        """
        return obj.tipo if obj.tipo else "Desconhecido"


class ManhwaListSerializer(ModelSerializer):
    capa_url = SerializerMethodField()
    calificacion_prom = SerializerMethodField()

    class Meta:
        model = Manhwa
        fields = ("id", "titulo", "tipo", "capa_url", "calificacion_prom")

    def get_capa_url(self, obj):
        """
        Retorna a URL da capa se existir.
        """
        if obj.capa:
            return obj.capa.url
        return None

    def get_calificacion_prom(self, obj):
        """
        Retorna a média de avaliações do manhwa.
        """
        avaliacoes = AvaliacaoMahhwa.objects.filter(manhwa=obj)
        if avaliacoes.exists():
            promedio = sum(avaliacao.puntuacao for avaliacao in avaliacoes) / avaliacoes.count()
            return round(promedio, 2)
        return None
