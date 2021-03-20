# Generated by Django 3.1.7 on 2021-03-20 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Class', models.CharField(max_length=100)),
                ('Mobile', models.BigIntegerField()),
                ('Email', models.EmailField(max_length=200)),
            ],
        ),
    ]
