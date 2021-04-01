from django.forms import ModelForm
from masterManagement.models import Book


class BookForm(ModelForm):
    """書籍のフォーム"""
    class Meta:
        model = Book
        fields = ('no', 'startDate', 'endDate', 'title', 'categoly')
