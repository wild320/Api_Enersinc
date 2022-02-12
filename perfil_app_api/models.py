from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager



class UserManager(BaseUserManager):
    def create_user(self,documento,nombres,password=None):
        if not documento:
            raise ValueError("Debes tener un Numero de documento")
        
        
        user=self.model(documento=documento,nombres=nombres)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,documento,password):
        
        user=self.create_user(documento,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        
        return user


class User(AbstractBaseUser, PermissionsMixin):
    tipo_documento = models.CharField(max_length=255)
    documento = models.IntegerField(unique=True)
    nombres =models.CharField(max_length=255)   
    apellidos =models.CharField(max_length=255)
    hobbie =models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'documento'
    REQUIRED_FIELD = ['nombres']
    
    def get_full_name(self):
       return self.nombres 
    
    def get_short_name(self):
       return self.nombres
    def __str__(self):
        return self.documento