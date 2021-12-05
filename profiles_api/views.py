from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            "Uses HTTP Methods as function (get, post, put, patch, delete)",
            "Is similar to a traditional django view",
            "Gives you the most control over you application logic",
            "Is mapped manually to URls"
        ]

        return Response({"msg": "Hello!", "an_apiview": an_apiview})
