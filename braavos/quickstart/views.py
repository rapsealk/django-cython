from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from rest_framework.request import Request
from rest_framework.response import Response

# from .bin.example_cython import primes as primes_func
# from .bin.hello import hello as primes_func
from braavos.quickstart.bin.example_cython import primes as primes_func
from braavos.quickstart.serializers import GroupSerializer, UserSerializer


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
        # primes = self._get_primse(n)
        primes = primes_func(n)
        return Response(primes)

    def _get_primse(self, n: int) -> "list[int]":
        """
        Return a list of prime numbers.
        """
        result = []
        for i in range(2, n):
            is_prime = True
            for j in range(2, i):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                result.append(i)
        return result
