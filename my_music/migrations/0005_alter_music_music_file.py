# Generated by Django 5.0.7 on 2024-08-16 21:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_music', '0004_alter_music_music_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='music_file',
            field=models.FileField(blank=True, null=True, upload_to='music_files/', validators=[django.core.validators.FileExtensionValidator(['mp3'])], verbose_name='music_file'),
        ),
    ]
