from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from .bin.example_cython import get_users, primes, raise_exception
from .serializers import GroupSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.AllowAny]


class PrimeNumberViewSet(viewsets.ViewSet):
    """
    API endpoint that allows prime numbers to be viewed or edited.
    """

    permission_classes = [permissions.AllowAny]

    def list(self, request: Request) -> Response:
        """
        Return a list of prime numbers.
        """
        n = int(request.query_params.get("n", 0))
        result = primes(n)
        groups = [{"id": group.id, "name": group.name} for group in Group.objects.all()]
        users = [{"id": user.id, "username": user.username, "email": user.email} for user in get_users()]
        return Response({"result": result, "groups": groups, "users": users})


class CythonExceptionViewSet(viewsets.ViewSet):
    """
    API endpoint that raises an exception.
    """

    permission_classes = [permissions.AllowAny]

    def list(self, request: Request) -> Response:
        """
        Raise an exception.
        """
        raise_exception()


class PythonExceptionViewSet(viewsets.ViewSet):
    """
    API endpoint that raises an exception.
    """

    permission_classes = [permissions.AllowAny]

    def list(self, request: Request) -> Response:
        """
        Raise an exception.
        """
        raise Exception("This is an exception")
