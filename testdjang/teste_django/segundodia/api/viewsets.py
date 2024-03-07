from rest_framework.viewsets import ModelViewSet
from .serializers import PessoaSerializer
from fabrica.models import PessoasBancoDeDados

class PessoaViewSet(ModelViewSet):
    serializer_class = PessoaSerializer
    queryset = PessoasBancoDeDados.objects.all()