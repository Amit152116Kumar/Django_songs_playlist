# Generated by Django 2.1.5 on 2019-02-17 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0014_remove_song_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='Cover',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
