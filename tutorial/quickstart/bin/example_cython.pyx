from django.contrib.auth.models import User


def primes(n: int) -> list[int]:
    result = []
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            result.append(i)
    return result


def get_users():
    users = User.objects.all()
    return users
