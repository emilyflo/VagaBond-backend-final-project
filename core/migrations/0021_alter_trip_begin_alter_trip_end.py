# Generated by Django 4.0.4 on 2022-05-01 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_alter_log_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='begin',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='trip',
            name='end',
            field=models.DateTimeField(),
        ),
    ]
