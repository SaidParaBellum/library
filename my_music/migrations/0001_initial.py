# Generated by Django 4.2.13 on 2024-07-10 14:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('year', models.IntegerField(verbose_name='Year')),
                ('Music_file', models.FileField(blank=True, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(['mp4'])], verbose_name='Music_file')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
            ],
        ),
    ]
