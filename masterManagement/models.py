from django.db import models

# Create your models here.


class Book(models.Model):
    """書籍"""
    no = models.IntegerField('No')
    startDate = models.DateField('読始日', blank=True, null=True)
    endDate = models.DateField('読始日', blank=True, null=True)
    title = models.CharField('タイトル', max_length=255)
    categoly = models.CharField('カテゴリ', max_length=255, blank=True)

    def __str__(self):
        return self.title


class Memo(models.Model):
    """メモ"""
    book = models.ForeignKey(
        Book, verbose_name='書籍', related_name='memos', on_delete=models.CASCADE)
    comment = models.TextField('メモ', blank=True)

    def __str__(self):
        return self.comment
