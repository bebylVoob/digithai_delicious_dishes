# Generated by Django 3.1 on 2021-04-11 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuisine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dishes',
            name='desc',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
