# Generated by Django 4.1.6 on 2023-02-15 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbalance',
            name='balance',
            field=models.FloatField(default=0),
        ),
    ]