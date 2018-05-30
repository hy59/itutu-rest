from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication

from .models import BooksInfo
from .serializers import BooksInfoSerializer
from .filters import BooksInfoFilter

# Create your views here.
class BooksInfoPagination(PageNumberPagination):
    """
    数据分页设置
    """
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class BooksInfoListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    图书分页，过滤，搜索的实现
    """
    queryset =BooksInfo.objects.all()
    serializer_class = BooksInfoSerializer
    pagination_class = BooksInfoPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = BooksInfoFilter
    search_fields = ('booktitle', 'call_num', 'authors')

