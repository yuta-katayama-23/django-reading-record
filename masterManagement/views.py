from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

# Create your views here.


from masterManagement.models import Book
from masterManagement.forms import BookForm


def book_list(request):
    """書籍の一覧"""
    # return HttpResponse('書籍の一覧')
    books = Book.objects.all().order_by('id')
    return render(request, 'masterManagement/book_list.html', {'books': books})


def book_edit(request, book_id=None):
    """書籍の編集"""
    # return HttpResponse('書籍の編集')
    if book_id:   # book_id が指定されている (修正時)
        book = get_object_or_404(Book, pk=book_id)
    else:         # book_id が指定されていない (追加時)
        book = Book()

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():    # フォームのバリデーション
            book = form.save(commit=False)
            book.save()
            return redirect('masterManagement:book_list')
    else:    # GET の時
        form = BookForm(instance=book)  # book インスタンスからフォームを作成

    return render(request, 'masterManagement/book_edit.html', dict(form=form, book_id=book_id))


def book_del(request, book_id):
    """書籍の削除"""
    return HttpResponse('書籍の削除')
