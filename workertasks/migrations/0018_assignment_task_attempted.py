# Generated by Django 2.1.3 on 2019-05-30 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workertasks', '0017_auto_20190501_0157'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='task_attempted',
            field=models.TextField(blank=True, null=True),
        ),
    ]