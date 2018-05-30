from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

User = get_user_model()


class UserRegSerializer(serializers.ModelSerializer):
    """
    用户注册
    """
    username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="用户已经存在")])

    mobile = serializers.CharField(label="手机号码", help_text="手机号码", required=True, allow_blank=False,
                                   validators=[UniqueValidator(queryset=User.objects.all(), message="手机号已经存在")])

    password = serializers.CharField(style={'input_type': 'password'}, help_text="密码", label="密码", write_only=True)

    class Meta:
        model = User
        fields = ("username", "mobile", "password")
