# Generated by Django 2.1.1 on 2019-07-16 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blackswan', '0008_auto_20190716_0044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.AddField(
            model_name='workflowexecution',
            name='username_pr',
            field=models.CharField(default='NA', max_length=256),
        ),
    ]
