# Generated by Django 3.2.5 on 2021-08-17 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('timetable', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=150)),
                ('photo_href', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
    ]
