# Generated by Django 5.0.7 on 2024-08-16 21:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_video', '0002_alter_video_video_file_favoritevideo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='video_files/', validators=[django.core.validators.FileExtensionValidator(['mp4', 'MOV'])], verbose_name='video_file'),
        ),
    ]
