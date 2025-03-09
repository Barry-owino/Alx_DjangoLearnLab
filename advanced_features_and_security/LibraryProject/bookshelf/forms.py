from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    class Meta:
        model =Book
        fields = ['title', 'author']

    def clean title(self):
        title = self.cleaned_data.get('title')
        if "<scritp>" in title:
            raise forms.ValidationError("Invalid input detected.")
        return title
