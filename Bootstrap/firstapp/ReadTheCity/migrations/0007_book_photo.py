# Generated by Django 5.0.1 on 2024-01-23 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReadTheCity', '0006_alter_profile_birth_alter_profile_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/books/', verbose_name='Фото'),
        ),
    ]