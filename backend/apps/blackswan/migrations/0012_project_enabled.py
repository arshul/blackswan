# Generated by Django 2.1.1 on 2019-07-16 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blackswan', '0011_auto_20190716_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='enabled',
            field=models.BooleanField(default=False),
        ),
    ]