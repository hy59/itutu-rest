from django_filters import rest_framework as filters

from .models import BooksInfo


class BooksInfoFilter(filters.FilterSet):
    """
    图书信息的过滤类
    """
    # 行为: 名称中包含某字符，且字符不区分大小写
    booktitle = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = BooksInfo
        fields = ['booktitle']
