# Generated by Django 3.1.3 on 2021-03-21 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicmap', '0002_auto_20210226_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchArtist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=100)),
            ],
        ),
    ]
