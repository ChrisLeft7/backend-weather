# Generated by Django 4.1.4 on 2022-12-22 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cast_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='forecast',
            name='notes',
            field=models.CharField(default='Great Place', max_length=32),
            preserve_default=False,
        ),
    ]
