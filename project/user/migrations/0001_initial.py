# Generated by Django 2.0.7 on 2018-07-21 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_photo', models.ImageField(upload_to='static/media')),
                ('profile_picture', models.ImageField(upload_to='static/media')),
                ('last_name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=200)),
                ('sex', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], default=True, max_length=6)),
                ('date_of_birth', models.DateField()),
                ('age', models.CharField(max_length=20)),
                ('student', models.BooleanField(default=True)),
                ('teacher', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]
