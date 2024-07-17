from django.db import models
from isbn_field import ISBNField

# Create your models here
class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200,)
    author = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='book_genre')
    synopsis = models.TextField(blank=True, null=True)
    publication_year = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    isbn = ISBNField()
    cover = models.ImageField(upload_to='books/', blank=True, null=True)

    def __str__(self) -> str:
        return self.title
