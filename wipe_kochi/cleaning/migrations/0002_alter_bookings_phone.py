# Generated by Django 5.0.2 on 2024-05-22 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cleaning', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]
