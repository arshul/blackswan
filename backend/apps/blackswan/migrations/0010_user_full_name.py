# Generated by Django 2.1.1 on 2019-07-16 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blackswan', '0009_auto_20190716_0045'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(default='name', max_length=30, verbose_name='Full name'),
        ),
    ]
