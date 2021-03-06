# Generated by Django 2.2.5 on 2019-10-28 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cost', models.IntegerField()),
                ('size', models.IntegerField()),
                ('person', models.IntegerField()),
                ('bed', models.CharField(max_length=50)),
                ('wifi', models.BooleanField()),
                ('tv', models.BooleanField()),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
