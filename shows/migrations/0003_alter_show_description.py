# Generated by Django 3.2.4 on 2021-06-25 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0002_alter_show_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='description',
            field=models.TextField(default='No description', null=True),
        ),
    ]
