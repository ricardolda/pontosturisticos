from rest_framework.viewsets import ModelViewSet
from avaliacoes.models import Avaliacao
from .serializers import AvaliacaoSerializer
from rest_framework.permissions import IsAuthenticated


class AvaliacaoViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    # queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        arquivo = open('avaliacao.txt', 'a')
        lista = Avaliacao.objects.all()
        arquivo.writelines(str(lista))
        arquivo.write('\n')
        arquivo.close()
        return Avaliacao.objects.all()

    def list(self, request, *args, **kwargs):
        arquivo = open('avaliacao.txt', 'a')
        lista = Avaliacao.objects.all()
        arquivo.writelines(str(lista))
        arquivo.write('\n')
        arquivo.close()
        return super(AvaliacaoViewSet, self).list(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        arquivo = open('avaliacao.txt', 'a')
        lista = Avaliacao.objects.all()
        arquivo.writelines(str(lista))
        arquivo.write('\n')
        arquivo.close()
        return super(AvaliacaoViewSet, self).destroy(request, *args, **kwargs)