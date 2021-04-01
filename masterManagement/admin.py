from django.contrib import admin
from masterManagement.models import Book, Memo
# Register your models here.


# admin.site.register(Book)
# admin.site.register(Memo)

class BookAdmin(admin.ModelAdmin):
    # 一覧に出したい項目
    list_display = ('id', 'startDate', 'endDate',
                    'title', 'categoly')
    # 修正リンクでクリックできる項目
    list_display_links = ('id', 'title',)


admin.site.register(Book, BookAdmin)


class MemoAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment',)
    list_display_links = ('id', 'comment',)
    raw_id_fields = ('book',)


admin.site.register(Memo, MemoAdmin)
