# Generated by Django 2.1.4 on 2019-01-07 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_invitation'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='blocked_contacts',
            field=models.ManyToManyField(related_name='profile_blocked_contacts', to='profiles.Profile'),
        ),
    ]
