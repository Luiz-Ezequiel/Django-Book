from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from books.views import books_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', books_view, name='books_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
