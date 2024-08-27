from rest_framework.viewsets import ModelViewSet

from core.models import Tipo
from core.serializers import TipoSerializer


class TipoViewSet(ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer
