# Generated by Django 3.0.7 on 2020-06-19 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0004_auto_20200619_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
    ]
