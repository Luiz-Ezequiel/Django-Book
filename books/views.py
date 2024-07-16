from django.shortcuts import render
from books.models import Book

# Create your views here.
def books_view(request):
    books = Book.objects.all().order_by('title')
    search = request.GET.get('search')
    if search != None:
        books = Book.objecs.filter(title__icontains=search)

    return render(request, 'books.html', {'books': books})
