from rest_framework.serializers import ModelSerializer, SlugRelatedField

from uploader.models import Image
from uploader.serializers import ImageSerializer

from core.models import Manhwa


class ManhwaSerializer(ModelSerializer):
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
        model = Manhwa
        fields = "__all__"


class ManhwaDetailSerializer(ModelSerializer):
    capa = ImageSerializer(required=False)
    
    class Meta:
        model = Manhwa
        fields = "__all__"
        depth = 1


class ManhwaListSerializer(ModelSerializer):
    class Meta:
        model = Manhwa
        fields = ("id", "titulo")
