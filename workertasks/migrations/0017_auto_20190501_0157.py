# Generated by Django 2.1.3 on 2019-05-01 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workertasks', '0016_task_number_of_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='tasks_available',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='assignment',
            name='tasks_recommended',
            field=models.TextField(blank=True, null=True),
        ),
    ]
