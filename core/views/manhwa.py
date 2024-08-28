from rest_framework.viewsets import ModelViewSet

from core.models import Manhwa
from core.serializers import ManhwaDetailSerializer, ManhwaListSerializer, ManhwaSerializer


class ManhwaViewSet(ModelViewSet):
    queryset = Manhwa.objects.order_by("titulo")
    serializer_class = ManhwaSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ManhwaListSerializer
        elif self.action == "retrieve":
            return ManhwaDetailSerializer
        return ManhwaSerializer
