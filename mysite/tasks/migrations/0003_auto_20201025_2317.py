# Generated by Django 3.0.3 on 2020-10-26 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20201025_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='num_users',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='points_awarded',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='time_completed',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='time_taken',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
