# Generated by Django 3.2.23 on 2023-12-18 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserAccountManagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(null=True),
        ),
    ]
