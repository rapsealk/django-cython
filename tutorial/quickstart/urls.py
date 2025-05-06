from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"primes", views.PrimeNumberViewSet, basename="prime")
router.register(r"cython-exception", views.CythonExceptionViewSet, basename="cython-exception")
router.register(r"python-exception", views.PythonExceptionViewSet, basename="python-exception")

urlpatterns = router.urls
