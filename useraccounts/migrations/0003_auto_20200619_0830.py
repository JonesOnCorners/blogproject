# Generated by Django 3.0.7 on 2020-06-19 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0002_auto_20200619_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='media/images/profile_pics/default.jpg', upload_to='media/images/profile_pics/'),
        ),
    ]
