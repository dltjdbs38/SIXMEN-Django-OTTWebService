# Generated by Django 3.2.6 on 2022-01-04 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('small_theater', '0002_auto_20220104_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smalltheater',
            name='introduce',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='smalltheater',
            name='notice',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='smalltheater',
            name='theater_owner',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='smalltheater',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
