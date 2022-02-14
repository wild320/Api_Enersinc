from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from perfil_app_api import serializers,models
from rest_framework.permissions import IsAuthenticated

from perfil_app_api import serializers


class PersonaApiView(APIView):

    serializer_class = serializers.UsuarioSerializer
    
    def get(self, request,format=None):
        an_apiview = [
            'aqui va el api view'
            ]
        return Response({'message':'hello','an_apiview':an_apiview})
    
    def post(self,request):
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('nombres')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request, pk=None):
        return Response({'method':'PUT'})

    def patch(self,request, pk=None):
        return Response({'method':'PATCH'})
    
    def delete(self,request, pk=None):
        return Response({'method':'DELETE'})


    
class UserProfileViewSet(viewsets.ModelViewSet):
    '''Crea y actualiza Usuarios'''
    serializer_class = serializers.UsuarioSerializer
    queryset = models.User.objects.all().order_by('id')
    
