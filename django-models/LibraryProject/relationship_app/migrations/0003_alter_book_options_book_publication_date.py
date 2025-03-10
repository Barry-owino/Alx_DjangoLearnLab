# Generated by Django 5.1.6 on 2025-03-05 18:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('can_add_book', 'Can add a nee book'), ('can_change_book', 'Can modify existing book details'), ('can_delete_book', 'Can delete a book from the library')]},
        ),
        migrations.AddField(
            model_name='book',
            name='publication_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
