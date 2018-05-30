import sys
import os

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "itutu.settings")

import django

django.setup()

from books.models import BooksInfo
from db_tools.data.booksinfo_data01 import row_data

# 导入数据
for booksinfo_detail in row_data:
    booksinfo = BooksInfo()
    booksinfo.ISBN = booksinfo_detail["ISBN"]
    booksinfo.booktitle = booksinfo_detail["booktitle"]
    booksinfo.authors = booksinfo_detail["authors"]
    booksinfo.pub_house = booksinfo_detail["pub_house"]
    booksinfo.pub_date = booksinfo_detail["pub_date"]
    booksinfo.call_num = booksinfo_detail["call_num"]
    booksinfo.save()
