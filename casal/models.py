from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Casal(models.Model):
    usuario1 = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
        related_name = 'criar_casal' 
    )

    usuario2 = models.OneToOneField(
        User,
        on_delete = models.SET_NULL,
        related_name = 'companheiro_casal' ,
        null = True,
        blank = True,
    )

    codigo_convite = models.CharField(max_length=8, unique= True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Casal {self.id_casal}: {self.usuario1} e {self.usuario2}"
    