# Generated by Django 4.2.1 on 2023-05-23 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='joined_date',
            field=models.DateField(null=True),
        ),
    ]
