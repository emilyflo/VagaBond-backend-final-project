# Generated by Django 4.0.4 on 2022-05-04 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_remove_image_log_image_log_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='subscribers',
            field=models.ManyToManyField(blank=True, related_name='trip_subscribers', to='core.contacts'),
        ),
    ]
