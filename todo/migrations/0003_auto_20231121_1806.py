# Generated by Django 3.2.9 on 2023-11-21 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='taskname',
            field=models.CharField(max_length=200),
        ),
    ]
