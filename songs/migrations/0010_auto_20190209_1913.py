# Generated by Django 2.1.5 on 2019-02-09 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0009_auto_20190209_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='Album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='songs.Album'),
        ),
        migrations.AlterField(
            model_name='song',
            name='Composer',
            field=models.ManyToManyField(blank=True, null=True, related_name='Composer', to='songs.Artist'),
        ),
        migrations.AlterField(
            model_name='song',
            name='Singer',
            field=models.ManyToManyField(blank=True, null=True, related_name='Singer', to='songs.Artist'),
        ),
    ]
