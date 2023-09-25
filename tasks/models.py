from django.db import models
from django.contrib.auth.models import (AbstractUser,PermissionsMixin)
from django.db import models

class Estudiante(AbstractUser,PermissionsMixin):
    codigo_estudiante = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=100)
    REQUIRED_FIELDS=[]
    USERNAME_FIELD='codigo_estudiante'
    PASSWORD_FIELD = 'contraseña'



    def __str__(self):
        return self.codigo_estudiante