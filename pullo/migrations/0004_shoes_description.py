# Generated by Django 3.1.7 on 2021-03-21 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pullo', '0003_shoes_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoes',
            name='description',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
    ]