# Generated by Django 5.0.1 on 2024-01-23 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReadTheCity', '0008_book_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='like',
            field=models.IntegerField(default=0, verbose_name='Количество в избранном'),
        ),
        migrations.AddField(
            model_name='profile',
            name='books',
            field=models.ManyToManyField(to='ReadTheCity.book', verbose_name='Избранное'),
        ),
    ]
