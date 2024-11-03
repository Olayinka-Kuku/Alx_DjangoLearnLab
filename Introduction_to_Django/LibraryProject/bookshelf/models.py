from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)        # Title of the book, max 200 characters
    author = models.CharField(max_length=100)       # Author name, max 100 characters
    publication_year = models.IntegerField()        # Year of publication

    def __str__(self):
        return self.title