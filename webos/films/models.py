from django.db import models


# Create your models here.
class AllFilms(models.Model):
    MY_CHOICES = (
        ('Фильм', 'Фильм'),
        ('Сериал', 'Сериал'),
        ('Мультфильм', 'Мультфильм')
    )
    Type = models.CharField('Тип (Фильм, Сериал, Мультфильм)', max_length=10, choices=MY_CHOICES)
    Name_of_film = models.CharField('Название', max_length=50)
    Image_of_film = models.ImageField('Картинка', upload_to='image/%Y-%m-%d/', null=True, blank=True)
    Image_name_of_film = models.ImageField('Картинка названия', upload_to='image_name/%Y-%m-%d/', null=True, blank=True)
    Trailer_of_film = models.FileField('Трейлер', upload_to='trailers/%Y-%m-%d/')
    Video_of_film = models.FileField('Видео', upload_to='video/%Y-%m-%d/')
    Category = models.CharField('Категория', max_length=25)
    Director = models.CharField('Режиссер', max_length=25)
    Time = models.CharField('Продолжительность (часы и минуты)', max_length=25)
    Year = models.CharField('Год выпуска', max_length=25)
    Actors = models.TextField('Актеры')
    Description = models.TextField('Описание')

    def __str__(self):
        return self.Name_of_film

    def get_absolute_url(self):
        return f'/films/{self.id}'

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
