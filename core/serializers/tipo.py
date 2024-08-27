from rest_framework.serializers import ModelSerializer

from core.models import Tipo


class TipoSerializer(ModelSerializer):
    class Meta:
        model = Tipo
        fields = "__all__"
