# Generated by Django 2.1.5 on 2019-02-09 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0002_auto_20190204_1417'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actor',
            options={'ordering': ['Title']},
        ),
        migrations.AlterModelOptions(
            name='artist',
            options={'ordering': ['Title']},
        ),
        migrations.RenameField(
            model_name='actor',
            old_name='Name',
            new_name='Title',
        ),
        migrations.RenameField(
            model_name='artist',
            old_name='Name',
            new_name='Title',
        ),
    ]
