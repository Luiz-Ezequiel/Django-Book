from django import forms
from books.models import Genre, Book

class BookForm(forms.Form):
    title = forms.CharField(max_length=200)
    author = forms.CharField(max_length=200)
    genre = forms.ModelChoiceField(Genre.objects.all())
    synopsis = forms.CharField(widget=forms.Textarea())
    publication_year = forms.IntegerField()
    price = forms.FloatField()
    cover = forms.ImageField()

    def save(self):
        book = Book(
            title = self.cleaned_data['title'],
            author = self.cleaned_data['author'],
            genre = self.cleaned_data['genre'],
            synopsis = self.cleaned_data['synopsis'],
            publication_year = self.cleaned_data['publication_year'],
            price = self.cleaned_data['price'],
            cover = self.cleaned_data['cover'],
        )
        book.save()
        return book
