# Generated by Django 4.2.13 on 2024-07-05 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_popupstore_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stamp',
            old_name='created_at',
            new_name='date_received',
        ),
    ]
