from rest_framework.viewsets import ModelViewSet

from core.models import Manga
from core.serializers import MangaDetailSerializer, MangaListSerializer, MangaSerializer


class MangaViewSet(ModelViewSet):
    queryset = Manga.objects.order_by("titulo")
    serializer_class = MangaSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MangaListSerializer
        elif self.action == "retrieve":
            return MangaDetailSerializer
        return MangaSerializer
