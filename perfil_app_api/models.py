from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Create your models here.
class UserManager(BaseUserManager):
    def create(self,tipo_documento,documento,nombres,apellidos,hobbie):
        if not documento:
            raise ValueError("Debes tener un Numero de documento")
        
        user=self.model(tipo_documento=tipo_documento,documento=documento,nombres=nombres,apellidos=apellidos,hobbie=hobbie)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    tipo_documento = models.CharField(max_length=255)
    documento = models.IntegerField(unique=True)
    nombres =models.CharField(max_length=255)   
    apellidos =models.CharField(max_length=255)
    hobbie =models.CharField(max_length=255)
    activado=models.BooleanField(default=True)
    objects = UserManager()
    USERNAME_FIELD = 'documento'
    REQUIRED_FIELD = ['nombres']
    
    def get_full_name(self):
       return self.nombres 
    
    def get_short_name(self):
       return self.nombres
    def __str__(self):
        return self.documento