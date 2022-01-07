# Generated by Django 3.2.6 on 2022-01-07 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SmallTheater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_date', models.DateField()),
                ('title', models.CharField(default='', max_length=200)),
                ('theater_owner', models.CharField(max_length=10, null=True)),
                ('theater_genre1', models.CharField(max_length=30, null=True)),
                ('theater_genre2', models.CharField(max_length=30, null=True)),
                ('introduce', models.CharField(max_length=1000, null=True)),
                ('notice', models.CharField(max_length=1000, null=True)),
            ],
            options={
                'db_table': 'small_theater',
            },
        ),
    ]
