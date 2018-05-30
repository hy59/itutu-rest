from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

from rest_framework.mixins import CreateModelMixin
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from .serializers import UserRegSerializer

User = get_user_model()


# Create your views here.
class CustomBackend(ModelBackend):
    """
    自定义用户验证规则
    """

    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(
                Q(username=username) | Q(mobile=username))
            # django的后台中密码加密：所以不能password==password
            # UserProfile继承的AbstractUser中有def check_password(self,
            # raw_password):
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class UserViewset(CreateModelMixin, viewsets.GenericViewSet):
    """
    用户
    """
    serializer_class = UserRegSerializer
    queryset = User.objects.all()

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = self.perform_create(serializer)
    #
    #     re_dict = serializer.data
    #     payload = jwt_payload_handler(user)
    #     re_dict["token"] = jwt_encode_handler(payload)
    #     re_dict["name"] = user.name if user.name else user.username
    #
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)
