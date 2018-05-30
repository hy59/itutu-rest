"""itutu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from itutu.settings import MEDIA_ROOT

import xadmin
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

from books.views import BooksInfoListViewSet
from users.views import UserViewset

# Create a router and register our viewsets with it.
router = DefaultRouter()
# 配置 goods 的 url
router.register(r'booksinfo', BooksInfoListViewSet, base_name='booksinfo')

# 配置 users 的 url
router.register(r'users', UserViewset, base_name='users')

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),

    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),

    # 自动化文档
    path('docs/', include_docs_urls(title='itutu')),

    # 调试登录
    path('api-auth/', include('rest_framework.urls')),

    # drf 自带的 token 授权登录,获取 token 需要向该地址 post 数据
    path('api-token-auth/', views.obtain_auth_token),

    # router的path路径
    re_path('^', include(router.urls)),

    # jwt 的 token 认证
    path('login/', obtain_jwt_token),

]
