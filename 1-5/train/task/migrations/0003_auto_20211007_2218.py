# Generated by Django 3.2.3 on 2021-10-07 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_alter_task_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='nlatin',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='task',
            name='rinci',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='task',
            name='item',
            field=models.CharField(default='', max_length=30),
        ),
    ]
