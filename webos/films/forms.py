from fileinput import FileInput

from .models import AllFilms
from django.forms import ModelForm, TextInput, Textarea, ImageField, FileField
from django import forms


class AllFilmsForm(ModelForm):
    class Meta:
        model = AllFilms
        fields = ['Type', 'Name_of_film', 'Image_of_film', 'Image_name_of_film', 'Trailer_of_film', 'Video_of_film',
                  'Category', 'Director', 'Time', 'Year', 'Actors', 'Description']

        widgets = {
            'Type': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тип (Фильм, Сериал, Мультфильм)'
            }),
            'Name_of_film': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            'Image_of_film': forms.FileInput(attrs={
                'class': 'common_class',
                'placeholder': 'Картинка'
            }),
            'Image_name_of_film': forms.FileInput(attrs={
                'class': 'common_class',
                'placeholder': 'Картинка названия'
            }),
            'Trailer_of_film': forms.FileInput(),
            'Video_of_film': forms.FileInput,
            'Category': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Категория'
            }),
            'Director': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Режиссер'
            }),
            'Time': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Продолжительность (часы и минуты)'
            }),
            'Year': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Год выпуска'
            }),
            'Actors': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Актеры'
            }),
            'Description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
        }
