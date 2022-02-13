from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from perfil_app_api import serializers


class PersonaApiView(APIView):

    serializer_class = serializers.HelloSerializer
    
    def get(self, request,format=None):
        an_apiview = [
            'aqui va el api view'
            ]
        return Response({'message':'hello','an_apiview':an_apiview})
    
    def post(self,request):
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            nombres = serializer.validated_data.get('nombres')
            message = f'Hello {nombres}'
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


class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer
    
    def list(self,request):
        a_viewset = [
            'usa acciones, mapea',
        ]
        return Response({'message':'Hola!','a_viewset': a_viewset})

    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            nombres =serializer.validated_data.get('nombres')
            message = f'Hola {nombres}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def retrieve(self,request,pk=None):
        return Response({'http_method':'GET'})
    
    def update(self,request,pk=None):
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        return Response({'http_method':'DELETE'})

    

      