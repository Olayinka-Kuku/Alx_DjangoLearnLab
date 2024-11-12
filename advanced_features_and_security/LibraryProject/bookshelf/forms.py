from django import forms

class BookSearchForm(forms.Form):
    search_term = forms.CharField(max_length=255)
