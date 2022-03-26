from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """ Criando um custom usuário, baseado no usuário padrão do Django """
    TYPES = (
        ('I','Interno'),
        ('P','Parceiro')
    )

    user_type = models.CharField(max_length=1, choices=TYPES, default='P', blank=False, null=False)
