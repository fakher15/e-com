# Generated by Django 3.1.7 on 2021-03-20 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pullo', '0002_auto_20210319_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoes',
            name='rate',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
