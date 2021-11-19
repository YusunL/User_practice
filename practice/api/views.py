from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializer import UserSerializer
from app.models import User

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer

# 회원가입, 로그인, 로그아웃


class UserViewSet(CreateModelMixin,
                  GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny, IsAuthenticated]


