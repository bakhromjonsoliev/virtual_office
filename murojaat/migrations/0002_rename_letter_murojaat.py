# Generated by Django 5.0.6 on 2024-05-21 03:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('murojaat', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Letter',
            new_name='Murojaat',
        ),
    ]