# Generated by Django 2.0.7 on 2018-07-19 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repo', '0003_uploadmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadmodel',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uploadmodel',
            name='update_changes',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
