from rest_framework.viewsets import ModelViewSet
from comentarios.models import Comentario
from .serializers import ComentarioSerializer
from rest_framework.permissions import IsAuthenticated


class ComentarioViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    # queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

    def get_queryset(self):
        arquivo = open('comentario.txt', 'a')
        lista = Comentario.objects.all()
        arquivo.writelines(str(lista))
        arquivo.write('\n')
        arquivo.close()
        return Comentario.objects.all()

    def list(self, request, *args, **kwargs):
        arquivo = open('comentario.txt', 'a')
        lista = Comentario.objects.all()
        arquivo.writelines(str(lista))
        arquivo.write('\n')
        arquivo.close()
        return super(ComentarioViewSet, self).list(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        arquivo = open('comentario.txt', 'a')
        lista = Comentario.objects.all()
        arquivo.writelines(str(lista))
        arquivo.write('\n')
        arquivo.close()
        return super(ComentarioViewSet, self).destroy(request, *args, **kwargs)