# Generated by Django 4.0.4 on 2022-05-06 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(blank=True, choices=[('action', 'Экшен'), ('adventure', 'Приключения'), ('comedy', 'Комедия'), ('drama', 'Драма'), ('fantasy', 'Фэнтези'), ('horror', 'Ужасы')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.TextField(blank=True, null=True),
        ),
    ]
