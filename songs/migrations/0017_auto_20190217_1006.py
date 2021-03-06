# Generated by Django 2.1.5 on 2019-02-17 04:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('songs', '0016_auto_20190217_0824'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(default='Media/default/profile.png', null=True, upload_to='')),
                ('Username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='album',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songs.Profile'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songs.Profile'),
        ),
        migrations.AlterField(
            model_name='song',
            name='Artist',
            field=models.ManyToManyField(blank=True, to='songs.Artist'),
        ),
        migrations.AlterField(
            model_name='song',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songs.Profile'),
        ),
    ]
