# Generated by Django 5.0.6 on 2024-07-04 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('popplace', '0014_remove_popupstore_operating_period'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='participant',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
