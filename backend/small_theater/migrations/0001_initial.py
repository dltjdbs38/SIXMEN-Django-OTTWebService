# Generated by Django 3.2.6 on 2022-01-04 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SmallTheater',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('published_date', models.DateField()),
                ('title', models.CharField(max_length=200)),
                ('theater_owner', models.CharField(max_length=10)),
                ('theater_genre1', models.CharField(max_length=30)),
                ('introduce', models.CharField(max_length=1000)),
                ('notice', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'small_theater',
            },
        ),
    ]
