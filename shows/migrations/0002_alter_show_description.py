# Generated by Django 3.2.4 on 2021-06-25 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
