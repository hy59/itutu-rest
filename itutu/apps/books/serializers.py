from rest_framework import serializers

from .models import BooksInfo


class BooksInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksInfo

        # 调用所有属性
        fields = '__all__'
