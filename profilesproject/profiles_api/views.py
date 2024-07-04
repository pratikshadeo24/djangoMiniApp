from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test Api View"""

    def get(self, request, format=None):
        """Returns a list of Api view features""" 
        an_apiview = [
            'Uses api methods a function (get, post, put, patch, delete)',
            'It is similar to a traditional django view', 
            'Gives you most control over your application logic',
            'Is mapped manually to urls'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
# Create your views here.
