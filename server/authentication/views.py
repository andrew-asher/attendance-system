from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
import jwt
from django.conf import settings

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = User.objects.get(username=username, password=password)
            payload = {'username': user.username}
            token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
            return Response({'token': token}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
