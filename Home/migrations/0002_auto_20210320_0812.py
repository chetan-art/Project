# Generated by Django 3.1.7 on 2021-03-20 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addstudent',
            name='Mobile',
            field=models.BigIntegerField(),
        ),
    ]
