from django.contrib import admin
from books.models import Book, Genre

# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'cover',
        'author',
        'synopsis',
        'publication_year',
        'price',
        'isbn',
    )
    search_fields = ('title',)

admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)
