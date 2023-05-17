from tortoise.models import Model
from tortoise import fields

class Jogos(Model):
    nome = fields.CharField(max_length=20)
    categoria = fields.CharField(max_length=20)
    console = fields.CharField(max_length=20)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.nome
