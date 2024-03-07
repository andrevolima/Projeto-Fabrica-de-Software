#fabrica
from django.db import models

class PessoasBancoDeDados(models.Model):
    primeiro_nome = models.CharField(verbose_name="Meu primeiro nome", max_length=50)
    segundo_nome = models.CharField(verbose_name="Meu segundo nome", max_length=80)
    idade = models.IntegerField(verbose_name="Minha Idade", blank=True, null=True)

    def __str__ (self) -> str:
        return f"{self.primeiro_nome} {self.segundo_nome}"