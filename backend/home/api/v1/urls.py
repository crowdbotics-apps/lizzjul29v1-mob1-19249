from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    A01234567890123456789012345678901234567890123456789ViewSet,
    A01234567890123456789012345678901234567890123456789012345678901234567890123456789ViewSet,
    CustomTextViewSet,
    HomePageViewSet,
)

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
    HomePageViewSet,
    CustomTextViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("customtext", CustomTextViewSet)
router.register("homepage", HomePageViewSet)
router.register(
    "a01234567890123456789012345678901234567890123456789012345678901234567890123456789",
    A01234567890123456789012345678901234567890123456789012345678901234567890123456789ViewSet,
)
router.register(
    "a01234567890123456789012345678901234567890123456789",
    A01234567890123456789012345678901234567890123456789ViewSet,
)

urlpatterns = [
    path("", include(router.urls)),
]
