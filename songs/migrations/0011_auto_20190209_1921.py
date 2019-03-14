# Generated by Django 2.1.5 on 2019-02-09 13:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('songs', '0010_auto_20190209_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artist',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='song',
            name='Album',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='songs.Album'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='song',
            name='Singer',
            field=models.ManyToManyField(blank=True, related_name='Singer', to='songs.Artist'),
        ),
    ]