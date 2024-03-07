from rest_framework.serializers import ModelSerializer
from fabrica.models import PessoasBancoDeDados

class PessoaSerializer(ModelSerializer):
    class Meta:
        model = PessoasBancoDeDados
        fields = ['id','primeiro_nome','segundo_nome','idade']
