from django import forms

class ExampleForm(forms.Form):
    search_term = forms.CharField(max_length=255)

