from rest_framework.viewsets import ModelViewSet
from endereco.models import Endereco
from .serializers import EnderecoSerializer
from rest_framework.permissions import IsAuthenticated


class EnderecoViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
