from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.permissions import IsAuthenticated


class PontoTuristicoViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    """
    A simple ViewSet for viewing and editing accounts.
    """
    # queryset = PontoTuristico.objects.filter(aprovado=True)
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        arquivo = open('acore.txt','a')
        lista = PontoTuristico.objects.all()
        arquivo.writelines(str(lista))
        arquivo.write('\n')
        arquivo.close()
        return PontoTuristico.objects.all()

    def list(self, request, *args, **kwargs):
        arquivo = open('acore.txt', 'a')
        lista = PontoTuristico.objects.all()
        arquivo.writelines(str(lista))
        arquivo.write('\n')
        arquivo.close()
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        arquivo = open('acore.txt', 'a')
        lista = PontoTuristico.objects.all()
        arquivo.writelines(str(lista))
        arquivo.write('\n')
        arquivo.close()
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        arquivo = open('acore.txt', 'a')
        lista = PontoTuristico.objects.all()
        arquivo.writelines(str(lista))
        arquivo.write('\n')
        arquivo.close()
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        arquivo = open('acore.txt', 'a')
        lista = PontoTuristico.objects.all()
        arquivo.writelines(str(lista))
        arquivo.write('\n')
        arquivo.close()
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        arquivo = open('acore.txt', 'a')
        lista = PontoTuristico.objects.all()
        arquivo.writelines(str(lista))
        arquivo.write('\n')
        arquivo.close()
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        arquivo = open('acore.txt', 'a')
        lista = PontoTuristico.objects.all()
        arquivo.writelines(str(lista))
        arquivo.write('\n')
        arquivo.close()
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    @action(methods=['post', 'get'], detail=True)
    def denunciar(self, request, pk=None):
        pass

    @action(methods=['get'], detail=False)
    def teste(self, request):
        pass


