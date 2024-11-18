from rest_framework.serializers import ModelSerializer, SlugRelatedField, SerializerMethodField
from uploader.models import Image
from uploader.serializers import ImageSerializer
from core.models import Livro, AvaliacaoLivro

class LivroSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)
    completo = SerializerMethodField()  # Campo completo
    calificacion_promedio = SerializerMethodField()  # Calificación promedio

    class Meta:
        model = Livro
        fields = "__all__"

    def get_completo(self, obj):
        return obj.completo  # Retorna el valor del campo 'completo'

    def get_calificacion_promedio(self, obj):
        avaliacoes = AvaliacaoLivro.objects.filter(livro=obj)
        if avaliacoes.exists():
            promedio = sum(avaliacao.puntuacao for avaliacao in avaliacoes) / avaliacoes.count()
            return round(promedio, 2)  # Devuelve el promedio redondeado a 2 decimales
        return None  # Si no hay evaluaciones, retorna None o 0 según prefieras


class LivroDetailSerializer(ModelSerializer):
    capa = ImageSerializer(required=False)
    completo = SerializerMethodField()  # Campo completo
    calificacion_promedio = SerializerMethodField()  # Calificación promedio

    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1  # Esto incluye las relaciones anidadas como la imagen

    def get_completo(self, obj):
        return obj.completo  # Retorna el valor del campo 'completo'

    def get_calificacion_promedio(self, obj):
        # Calcula el promedio de las puntuaciones de las evaluaciones relacionadas con el libro
        avaliacoes = AvaliacaoLivro.objects.filter(livro=obj)
        if avaliacoes.exists():
            promedio = sum(avaliacao.puntuacao for avaliacao in avaliacoes) / avaliacoes.count()
            return round(promedio, 2)  # Devuelve el promedio redondeado a 2 decimales
        return None  # Si no hay evaluaciones, retorna None o 0 según prefieras


class LivroListSerializer(ModelSerializer):
    completo = SerializerMethodField()  # Campo completo
    calificacion_promedio = SerializerMethodField()  # Calificación promedio

    class Meta:
        model = Livro
        fields = ("id", "titulo", "preco", "completo", "calificacion_promedio")

    def get_completo(self, obj):
        return obj.completo  # Retorna el valor del campo 'completo'

    def get_calificacion_promedio(self, obj):
        # Calcula el promedio de las puntuaciones de las evaluaciones relacionadas con el libro
        avaliacoes = AvaliacaoLivro.objects.filter(livro=obj)
        if avaliacoes.exists():
            promedio = sum(avaliacao.puntuacao for avaliacao in avaliacoes) / avaliacoes.count()
            return round(promedio, 2)  # Devuelve el promedio redondeado a 2 decimales
        return None  # Si no hay evaluaciones, retorna None o 0 según prefieras
