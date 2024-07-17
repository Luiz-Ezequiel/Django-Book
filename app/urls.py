from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from books.views import books_view, new_book_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', books_view, name='books_list'),
    path('new_book/', new_book_view, name='new_book')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
