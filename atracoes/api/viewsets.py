from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from .serializers import AtracaoSerializer
from rest_framework.permissions import IsAuthenticated

class AtracaoViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    # queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer

    def get_queryset(self):
        arquivo = open('atracoes.txt', 'a')
        lista = Atracao.objects.all()
        arquivo.writelines(str(lista))
        arquivo.write('\n')
        arquivo.close()
        return Atracao.objects.all()

    def list(self, request, *args, **kwargs):
        arquivo = open('atracoes.txt', 'a')
        lista = Atracao.objects.all()
        arquivo.writelines(str(lista))
        arquivo.write('\n')
        arquivo.close()
        return super(AtracaoViewSet, self).list(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        arquivo = open('atracoes.txt', 'a')
        lista = Atracao.objects.all()
        arquivo.writelines(str(lista))
        arquivo.write('\n')
        arquivo.close()
        return super(AtracaoViewSet, self).destroy(request, *args, **kwargs)