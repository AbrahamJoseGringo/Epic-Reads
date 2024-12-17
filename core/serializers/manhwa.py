from rest_framework.serializers import ( 
    ModelSerializer, 
    SlugRelatedField,
    ValidationError,
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
    calificacion_prom = SerializerMethodField()
    capa = SerializerMethodField()

    class Meta:
        model = Manhwa
        fields = "__all__"

    def get_calificacion_promedio(self, obj):
        avaliacoes = AvaliacaoMahhwa.objects.filter(livro=obj)
        if avaliacoes.exists():
            promedio = sum(avaliacao.puntuacao for avaliacao in avaliacoes) / avaliacoes.count()
            return round(promedio, 2) 

    def get_capa_url(self, obj):
       
        if obj.capa:
            return obj.capa.url  
        return None  

class ManhwaDetailSerializer(ModelSerializer):
    capa = ImageSerializer(required=False)
    calificacion_prom = SerializerMethodField()
    capa = SerializerMethodField()
    
    class Meta:
        model = Manhwa
        fields = "__all__"
        depth = 1
    def get_calificacion_prom(self, obj):
        avaliacoes = AvaliacaoMahhwa.objects.filter(manhwa=obj)
        if avaliacoes.exists():
            promedio =sum(avaliacoes.puntuaçao for avaliacao in avaliacoes) / avaliacoes.count()
            return round(promedio, 2)
        return None
        
class ManhwaListSerializer(ModelSerializer):
    class Meta:
        model = Manhwa
        fields = ("id", "titulo")
