# Generated by Django 4.1.5 on 2023-01-29 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_remove_userprofile_url_userprofile_qrcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='qrcode',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='organization',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='url',
            field=models.URLField(default=''),
        ),
    ]
