# Generated by Django 3.1.5 on 2021-04-25 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicmap', '0012_auto_20210425_1010'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date_added']},
        ),
    ]
