# Generated by Django 3.1.5 on 2021-04-25 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicmap', '0011_auto_20210424_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
