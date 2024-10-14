# Generated by Django 5.1.1 on 2024-10-14 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
        ('tasks', '0002_alter_taskmodel_labels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='labels',
            field=models.ManyToManyField(blank=True, null=True, related_name='labels', through='tasks.TaskLabelRelation', to='labels.labelmodel'),
        ),
    ]
