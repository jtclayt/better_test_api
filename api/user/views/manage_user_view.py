from rest_framework import generics, authentication, permissions
from ..serializers.user_serializer import UserSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        '''Retrieve and return auth user'''
        return self.request.user
