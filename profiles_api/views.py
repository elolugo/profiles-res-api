from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status #list of HTTP status codes

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
