# Generated by Django 2.2.2 on 2019-06-24 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='vote',
            field=models.IntegerField(default=0),
        ),
    ]
