# Generated by Django 3.0.5 on 2020-04-06 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0009_form_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='desc',
            field=models.CharField(default='', max_length=223),
        ),
        migrations.AlterField(
            model_name='form',
            name='email',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='form',
            name='gender',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='form',
            name='username',
            field=models.CharField(default='', max_length=50),
        ),
    ]
