from rest_framework import generics
from ..serializers.user_serializer import UserSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
