# Generated by Django 4.1.5 on 2023-05-20 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='marks',
            field=models.IntegerField(default=0),
        ),
    ]
