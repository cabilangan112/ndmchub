# Generated by Django 2.0.7 on 2018-07-23 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repo', '0003_auto_20180722_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repo',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
    ]
