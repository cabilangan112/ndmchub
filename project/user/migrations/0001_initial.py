# Generated by Django 2.0.7 on 2018-07-24 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=40, unique=True)),
                ('profile_picture', models.ImageField(blank=True, height_field='height_field', null=True, upload_to='static/media', width_field='width_field')),
                ('first_name', models.CharField(blank=True, max_length=40)),
                ('last_name', models.CharField(blank=True, max_length=40)),
                ('tagline', models.CharField(blank=True, max_length=140)),
                ('sex', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], default=True, max_length=6)),
                ('date_of_birth', models.DateField()),
                ('age', models.CharField(max_length=20)),
                ('Location', models.CharField(max_length=100)),
                ('Bio', models.TextField(blank=True, default=True)),
                ('student', models.BooleanField(default=False)),
                ('teacher', models.BooleanField(default=False)),
                ('office', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='org',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now_add=True)),
                ('private', models.BooleanField(default=False)),
                ('public', models.BooleanField(default=False)),
                ('member', models.ManyToManyField(to='user.Account')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]
