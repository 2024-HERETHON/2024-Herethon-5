# Generated by Django 5.0.6 on 2024-07-02 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('popplace', '0009_category_tag'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tag',
            new_name='Location',
        ),
    ]
