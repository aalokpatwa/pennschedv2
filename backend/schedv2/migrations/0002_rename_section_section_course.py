# Generated by Django 4.0.1 on 2022-04-07 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedv2', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='section',
            old_name='section',
            new_name='course',
        ),
    ]
