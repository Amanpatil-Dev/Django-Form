# Generated by Django 3.0.5 on 2020-04-06 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0004_remove_form_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='date',
            field=models.DateField(default=0),
            preserve_default=False,
        ),
    ]
