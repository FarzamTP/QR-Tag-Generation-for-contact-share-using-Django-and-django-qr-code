# Generated by Django 4.1.5 on 2023-01-29 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='url',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='qrcode',
            field=models.ImageField(default='', upload_to='media/<django.db.models.fields.related.OneToOneField>/qrcodes/'),
        ),
    ]