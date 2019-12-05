# Generated by Django 2.2.1 on 2019-11-28 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_verified_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='verified',
            name='code',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='verified',
            name='user',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]