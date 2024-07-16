# Generated by Django 5.0.7 on 2024-07-16 03:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_rename_books_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='book_genre', to='books.genre'),
            preserve_default=False,
        ),
    ]
