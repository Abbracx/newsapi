# Generated by Django 4.0.2 on 2022-02-18 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Author',
            new_name='Article',
        ),
    ]