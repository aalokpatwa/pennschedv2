# Generated by Django 4.0.1 on 2022-03-28 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(max_length=4)),
                ('number', models.IntegerField()),
                ('full_code', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('instructor', models.CharField(max_length=50)),
                ('labs', models.ManyToManyField(to='schedv2.Section')),
                ('recitations', models.ManyToManyField(to='schedv2.Section')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedv2.course')),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.CharField(help_text='String of days MTWRF', max_length=7)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedv2.section')),
            ],
        ),
    ]
