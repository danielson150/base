# Generated by Django 2.1.4 on 2019-01-28 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20190108_0601'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='media/icon_user.jpg', upload_to='media/%Y/%m/%d'),
        ),
    ]