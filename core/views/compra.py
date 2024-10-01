from rest_framework.viewsets import ModelViewSet

from core.models import Compra
from core.serializers import CompraSerializer, CriarEditarCompraSerializer, ListarCompraSerializer


class CompraViewSet(ModelViewSet):
    # queryset = Compra.objects.all()
    # serializer_class = CompraSerializer

    def get_serializer_class(self):
        if self.action in ("create", "update"):
            return CriarEditarCompraSerializer
        elif self.action == "list":
            return ListarCompraSerializer
        return CompraSerializer

    def get_queryset(self):
        usuario = self.request.user
        if usuario.is_superuser:
            return Compra.objects.all()
        if usuario.groups.filter(name="administradores"):
            return Compra.objects.all()
        return Compra.objects.filter(usuario=usuario)
