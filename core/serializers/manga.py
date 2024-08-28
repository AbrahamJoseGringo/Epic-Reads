from rest_framework.serializers import ModelSerializer, SlugRelatedField

from uploader.models import Image
from uploader.serializers import ImageSerializer

from core.models import Manga


class MangaSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(
        required=False,
        read_only=True
    )

    class Meta:
        model = Manga
        fields = "__all__"


class MangaDetailSerializer(ModelSerializer):
    capa = ImageSerializer(required=False)
    
    class Meta:
        model = Manga
        fields = "__all__"
        depth = 1


class MangaListSerializer(ModelSerializer):
    class Meta:
        model = Manga
        fields = ("id", "titulo")
