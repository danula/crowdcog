# Generated by Django 2.1.3 on 2019-03-11 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workertasks', '0006_auto_20190308_0049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='assignment_id',
            new_name='assignment_uid',
        ),
        migrations.AddField(
            model_name='question',
            name='condition_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='workertasks.Condition'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='question_uid',
            field=models.CharField(default=0, max_length=64, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='task_uid',
            field=models.CharField(default='1', max_length=64, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worker',
            name='worker_uid',
            field=models.CharField(default=1, max_length=64, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='question_id',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_id',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='worker',
            name='worker_id',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterUniqueTogether(
            name='question',
            unique_together={('question_id', 'task_id', 'condition_id')},
        ),
        migrations.AlterUniqueTogether(
            name='task',
            unique_together={('task_id', 'condition_id')},
        ),
    ]
