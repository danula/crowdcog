# Generated by Django 2.1.3 on 2018-11-09 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workertasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='status',
            field=models.IntegerField(choices=[(0, 'Started'), (1, 'Working'), (2, 'Completed'), (3, 'Abandoned')], default=0),
        ),
        migrations.AlterField(
            model_name='worker',
            name='status',
            field=models.IntegerField(choices=[(0, 'New'), (1, 'Working'), (2, 'Completed')], default=0),
        ),
    ]