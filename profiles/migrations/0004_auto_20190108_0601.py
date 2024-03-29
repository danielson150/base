# Generated by Django 2.1.4 on 2019-01-08 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_blocked_contacts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_invitations', to='profiles.Profile'),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_invitations', to='profiles.Profile'),
        ),
    ]
