# Generated by Django 4.1.6 on 2023-02-15 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_alter_userbalance_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=36)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('category', models.CharField(max_length=24)),
                ('amount', models.FloatField()),
                ('is_expense', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.userbalance')),
            ],
        ),
    ]
