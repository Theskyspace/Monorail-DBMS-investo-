# Generated by Django 2.2.3 on 2020-01-22 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stations', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=300)),
            ],
        ),
    ]
