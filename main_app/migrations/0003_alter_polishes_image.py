# Generated by Django 4.1.5 on 2023-01-26 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_polishes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polishes',
            name='image',
            field=models.CharField(max_length=400),
        ),
    ]