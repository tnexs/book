from django import forms
from .models import Books


class BooksForm(forms.ModelForm):


    class Meta:
        model = Books
        fields = ["name","authors","price"]

    def __str__(self) -> str:
        return self.name