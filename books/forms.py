from django import forms
from books.models import Book
from datetime import datetime

class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def clean_publication_year(self):
        publication_year = self.cleaned_data.get('publication_year')
        current_year = datetime.now().year
        if publication_year > current_year:
            self.add_error('publication_year', 'Insira um ano válido')
        return publication_year
