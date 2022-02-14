from rest_framework import serializers

from perfil_app_api import models

# class HelloSerializer(serializers.Serializer):
#     nombres = serializers.CharField(max_length=10)

class UsuarioSerializer   (serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id','tipo_documento','documento','nombres','apellidos','hobbie','password')
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style': {'input_type':'password'}

            }
        }
    def create(self,validated_data):
        user =models.User.objects.create_user(
            tipo_documento=validated_data['tipo_documento'],
            documento=validated_data['documento'],
            nombres=validated_data['nombres'],
            apellidos=validated_data['apellidos'],
            hobbie=validated_data['hobbie'],
            password=validated_data['password']
        )
        return user
    
    def update(self,instance,validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance,validated_data)
        