from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status #list of HTTP status codes

from rest_framework import viewsets

from profiles_api import serializers

class HelloApiView(APIView):
    """Simple Test API View response"""

    serializer_class = serializers.HelloSerializer # Accept only this data from the serializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methos as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview}) # Dictionary or List only

    def post(self, request):
        """ Create a hello message with our name """
        serializer = self.serializer_class(data=request.data) # Retrieves the configured serializer class and passes the content of the POST

        if serializer.is_valid(): # Checking if the data POSTed as input is valid according to the serializers
            name = serializer.validated_data.get('name') # Retrieving the name field in the request
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """ Handle updating an object """
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """ Handle a partial update of an object """
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """ Delete an object """
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """ Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """ Return a hello message """
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """ Create a new hello messages  """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None): #Equals to -> GET/{primarykey}
        """ Handle getting an object by its ID """
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None): #update a specific object
        """ Handle updating an object by its ID """
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None): #partial update a specific object
        """ Handle updating part of an object by its ID """
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None): #delete a specific object
        """ Handle removing an object by its ID """
        return Response({'http_method': 'DELETE'})
