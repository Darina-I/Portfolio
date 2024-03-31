import django.conf
from django.db import models
from django.urls import reverse
from django.conf import settings

from .validators import clean_isbn, clean_year, clean_date


# from django.contrib.auth.models import AbstractUser

class Author(models.Model):
    fio = models.CharField(max_length=80, verbose_name='ФИО')
    birth = models.DateField(verbose_name='Дата рождения',validators =[clean_date])
    death = models.DateField(verbose_name='Дата смерти', null=True, blank=True,validators =[clean_date])
    content = models.TextField(verbose_name='Краткое описание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.fio

    #для создание ссылок на конкретного автора
    def get_absolute_url(self):
        return reverse('this_author',kwargs={'author_id': self.pk})

class Language(models.Model):
    name = models.CharField(max_length=20, verbose_name='Наименование')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'

    def __str__(self):
        return self.name

class Print(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    city = models.CharField(max_length=30, verbose_name='Город')
    create_print = models.DateField(verbose_name='Дата основания')
    content = models.TextField(verbose_name='Краткое описание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=20, verbose_name='Наименование')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    authors = models.ManyToManyField(Author, verbose_name='Авторы')
    photo = models.ImageField(null=True, blank=True, upload_to="images/books/", verbose_name='Фото')
    content = models.TextField(verbose_name='Краткое содержание')
    print = models.ForeignKey(Print, on_delete=models.CASCADE, verbose_name='Издательство')
    year = models.CharField(max_length=4, verbose_name='Год выпуска',validators =[clean_year])
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name='Жанр')
    lang = models.ManyToManyField(Language, verbose_name='Языки')
    isbn = models.CharField(max_length=17, verbose_name='ISBN',validators =[clean_isbn])
    upload = models.IntegerField(default=0, verbose_name='Количество скачиваний')
    like = models.IntegerField(default=0, verbose_name='Количество в избранном')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    # для создание ссылок на конкретной книги
    def get_absolute_url(self):
        return reverse('this_book',kwargs={'book_id': self.pk})

    def __str__(self):
        return self.name
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    city = models.CharField(max_length=20,null=True,blank=True, verbose_name='Город')
    photo = models.ImageField(null=True, blank=True, upload_to="images/profile/",verbose_name='Фото')
    birth = models.DateField(null=True, verbose_name='Дата рождения',validators =[clean_date])
    content = content = models.TextField(null=True, blank=True, verbose_name='О себе')
    books = models.ManyToManyField(Book, verbose_name='Избранное')
