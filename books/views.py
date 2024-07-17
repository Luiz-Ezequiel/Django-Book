from django.shortcuts import render, redirect
from books.models import Book
from books.forms import BookModelForm

# Create your views here.
def books_view(request):
    books = Book.objects.all().order_by('title')
    search = request.GET.get('search')
    if search != None:
        books = Book.objects.filter(title__icontains=search)

    return render(request, 'books.html', {'books': books})

def new_book_view(request):
    if request.method == 'POST':
        new_book_form = BookModelForm(request.POST, request.FILES)
        if new_book_form.is_valid():
            new_book_form.save()
            return redirect('books_list')
    else:
        new_book_form = BookModelForm()

    return render(request, 'new_book.html', { 'new_book_form': new_book_form })
