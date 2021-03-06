# Generated by Django 3.2.6 on 2022-01-07 23:11

import apps.user.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreferOttContentGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('drama', models.IntegerField(blank=True, null=True)),
                ('comedy', models.IntegerField(blank=True, null=True)),
                ('action', models.IntegerField(blank=True, null=True)),
                ('thriller', models.IntegerField(blank=True, null=True)),
                ('romance', models.IntegerField(blank=True, null=True)),
                ('crime', models.IntegerField(blank=True, null=True)),
                ('adventure', models.IntegerField(blank=True, null=True)),
                ('animation', models.IntegerField(blank=True, null=True)),
                ('fantasy', models.IntegerField(blank=True, null=True)),
                ('family', models.IntegerField(blank=True, null=True)),
                ('sci_fi', models.IntegerField(blank=True, null=True)),
                ('mystery', models.IntegerField(blank=True, null=True)),
                ('horror', models.IntegerField(blank=True, null=True)),
                ('documentary', models.IntegerField(blank=True, null=True)),
                ('biography', models.IntegerField(blank=True, null=True)),
                ('history', models.IntegerField(blank=True, null=True)),
                ('music', models.IntegerField(blank=True, null=True)),
                ('short', models.IntegerField(blank=True, null=True)),
                ('sport', models.IntegerField(blank=True, null=True)),
                ('war', models.IntegerField(blank=True, null=True)),
                ('musical', models.IntegerField(blank=True, null=True)),
                ('reality_tv', models.IntegerField(blank=True, null=True)),
                ('western', models.IntegerField(blank=True, null=True)),
                ('game_show', models.IntegerField(blank=True, null=True)),
                ('talk_show', models.IntegerField(blank=True, null=True)),
                ('img_link', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('nickname', models.CharField(max_length=50, validators=[apps.user.validators.NickNameValidator()])),
                ('birthday', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=50, null=True)),
                ('watch_time', models.IntegerField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('prefer_ott_content_genres', models.ManyToManyField(to='user.PreferOttContentGenre')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
