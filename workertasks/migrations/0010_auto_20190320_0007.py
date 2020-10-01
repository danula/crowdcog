# Generated by Django 2.1.3 on 2019-03-20 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workertasks', '0009_worker_consent_given'),
    ]

    operations = [
        migrations.CreateModel(
            name='CognitiveTestCompletion',
            fields=[
                ('test_uid', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('test_id', models.CharField(max_length=64)),
                ('accuracy', models.FloatField(null=True)),
                ('rt', models.FloatField(null=True)),
                ('effect_accuracy', models.FloatField(null=True)),
                ('effect_rt', models.FloatField(null=True)),
                ('condition_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workertasks.Condition')),
            ],
        ),
        migrations.AddField(
            model_name='worker',
            name='flanker',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='worker',
            name='nback',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='worker',
            name='pointing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='worker',
            name='stroop',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='worker',
            name='taskswitching',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cognitivetestcompletion',
            name='worker_uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workertasks.Worker'),
        ),
        migrations.AlterUniqueTogether(
            name='cognitivetestcompletion',
            unique_together={('test_id', 'worker_uid')},
        ),
    ]
