from django.db import models
from django.forms import ModelForm
from django import forms

# Create your models here.
TITLE_CHOICE = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS','Ms.'),
)

# Cách trình bày 2
class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3, choices = TITLE_CHOICE)
    birth_date = models.DateField(blank=True, null = True)

class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField (Author)

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'title', 'birth_date']

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'authors']


#Cách trình bày 1:

# class AuthorForm(forms.form):
#     name = forms.CharField(max_length=100)
#     title = forms.CharField(max_length=3, widget = forms.Select(choices= TITLE_CHOICE))
#     birth_date = forms.DateField(required= False)

# class BookForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     authors = forms.ModelMultipleChoiceField(queryset = Author.objects.all())