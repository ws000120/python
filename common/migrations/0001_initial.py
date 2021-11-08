# Generated by Django 3.2.9 on 2021-11-06 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField(default=18, null=True)),
                ('phone_number', models.CharField(max_length=11, null=True)),
                ('creation_time', models.DateTimeField(default='2021-11-06 19:53:34')),
            ],
        ),
    ]
