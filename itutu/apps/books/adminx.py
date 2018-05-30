import xadmin
from .models import BooksInfo


class BooksInfoAdmin(object):
    list_display = [
        "ISBN", "booktitle", "authors", "pub_house", "pub_date",
        "call_num", "add_time"
    ]
    search_fields = [
        'booktitle',
    ]
    list_editable = [
        "booktitle",
    ]
    list_filter = [
        "ISBN", "booktitle", "authors", "pub_house", "pub_date",
        "call_num", "add_time"
    ]


xadmin.site.register(BooksInfo, BooksInfoAdmin)
