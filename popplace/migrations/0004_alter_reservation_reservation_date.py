# Generated by Django 5.0.4 on 2024-07-02 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('popplace', '0003_alter_reservation_reservation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='reservation_date',
            field=models.DateTimeField(default='<function now at 0x0000011C9B8649A0>'),
        ),
    ]
