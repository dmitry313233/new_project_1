from rest_framework import viewsets

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):  # 2 задание
    serializer_class = UserSerializer
    queryset = User.objects.all()
