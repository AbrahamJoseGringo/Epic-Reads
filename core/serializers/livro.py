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


# Ajuste de Estoque de Livro
class LivroAjustarEstoqueSerializer(serializers.Serializer):
    quantidade = serializers.IntegerField()

    def validate_quantidade(self, value):
        # Acessa o objeto livro no contexto do serializer
        livro = self.context.get("livro")
        if livro:
            nova_quantidade = livro.quantidade + value
            if nova_quantidade < 0:
                raise serializers.ValidationError("A quantidade em estoque não pode ser negativa.")
        return value


# Alteração de Preço de Livro
class LivroAlterarPrecoSerializer(Serializer):
    preco = DecimalField(max_digits=10, decimal_places=2)

    def validate_preco(self, value):
        """Valida se o preço é um valor positivo."""
        if value <= 0:
            raise ValidationError("O preço deve ser um valor positivo.")
        return value


# Serializer de Detalhes do Livro (com as avaliações e capa com URL)
class LivroDetailSerializer(ModelSerializer):
    completo = SerializerMethodField()  # Campo completo
    calificacion_promedio = SerializerMethodField()  # Calificación promedio
    capa_url = SerializerMethodField()  # Nova URL da capa

    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1  # Isso inclui as relações aninhadas, como a imagem

    def get_completo(self, obj):
        return obj.completo  # Retorna o valor do campo 'completo'

    def get_calificacion_promedio(self, obj):
        # Calcula o preço médio das avaliações relacionadas ao livro
        avaliacoes = AvaliacaoLivro.objects.filter(livro=obj)
        if avaliacoes.exists():
            promedio = sum(avaliacao.puntuacao for avaliacao in avaliacoes) / avaliacoes.count()
            return round(promedio, 2)  # Retorna o preço médio arredondado a 2 casas decimais
        return None  # Se não houver avaliações, retorna None

    def get_capa_url(self, obj):
        # Retorna a URL da capa, se ela existir
        if obj.capa:
            return obj.capa.url  # Retorna o caminho completo da URL da imagem
        return None  # Retorna None se não houver capa


# Serializer para a Listagem de Livros (com a URL da capa)
class LivroListSerializer(ModelSerializer):
    completo = SerializerMethodField()  
    calificacion_promedio = SerializerMethodField() 
    capa_url = SerializerMethodField()  # Nova URL da capa

    class Meta:
        model = Livro
        fields = ("id", "titulo", "preco", "completo", "calificacion_promedio", "capa_url")

    def get_completo(self, obj):
        return obj.completo  # Retorna o valor do campo 'completo'

    def get_calificacion_promedio(self, obj):
        # Calcula a média das avaliações
        avaliacoes = AvaliacaoLivro.objects.filter(livro=obj)
        if avaliacoes.exists():
            promedio = sum(avaliacao.puntuacao for avaliacao in avaliacoes) / avaliacoes.count()
            return round(promedio, 2)  # Retorna a média das avaliações arredondada a 2 casas decimais
        return None  # Se não houver avaliações, retorna None

    def get_capa_url(self, obj):
        # Retorna a URL da capa
        if obj.capa:
            return obj.capa.url  # Retorna o caminho completo da URL da imagem
        return None  # Retorna None se não houver capa


# Serializer Principal para Livro (com URL da capa)
class LivroSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,  # Não será exibido na resposta
    )
    completo = SerializerMethodField()  
    calificacion_promedio = SerializerMethodField()  # Calificación promedio
    capa_url = SerializerMethodField()  # Nova URL da capa

    class Meta:
        model = Livro
        fields = "__all__"

    def get_completo(self, obj):
        return obj.completo  # Retorna o valor do campo 'completo'

    def get_calificacion_promedio(self, obj):
        avaliacoes = AvaliacaoLivro.objects.filter(livro=obj)
        if avaliacoes.exists():
            promedio = sum(avaliacao.puntuacao for avaliacao in avaliacoes) / avaliacoes.count()
            return round(promedio, 2)  # Retorna o valor médio das avaliações
        return None  # Se não houver avaliações, retorna None

    def get_capa_url(self, obj):
        # Retorna a URL da capa
        if obj.capa:
            return obj.capa.url  # Retorna o caminho completo da URL da imagem
        return None  # Retorna None se não houver capa
