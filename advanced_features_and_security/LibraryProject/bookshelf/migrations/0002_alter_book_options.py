# Generated by Django 5.1.6 on 2025-03-08 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('can_view', 'Can view book'), ('can_create', 'Can create book'), ('can_edit', 'Can edit book'), ('can_delete', 'Can delete book')]},
        ),
    ]
