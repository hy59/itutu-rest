from datetime import datetime

from django.db import models


# Create your models here.
class BooksInfo(models.Model):
    """
    图书基本信息
    """
    ISBN = models.CharField(max_length=100, verbose_name="ISBN", help_text="ISBN")
    booktitle = models.CharField(max_length=100, verbose_name="图书标题", help_text="图书标题")
    authors = models.CharField(max_length=100, verbose_name="作者", help_text="作者")
    pub_house = models.CharField(max_length=100, verbose_name="出版社", help_text="出版社")
    pub_date = models.CharField(max_length=100, verbose_name="出版日期", help_text="出版日期")
    call_num = models.CharField(max_length=100, verbose_name="索书号", help_text="索书号")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "图书信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.booktitle

