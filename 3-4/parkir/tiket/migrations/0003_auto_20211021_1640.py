# Generated by Django 3.2.3 on 2021-10-21 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiket', '0002_auto_20211021_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notempat', models.TextField(default='', max_length=5)),
                ('dtg', models.TimeField(blank=True, null=True)),
                ('klr', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='park',
            name='dtg',
        ),
        migrations.RemoveField(
            model_name='park',
            name='klr',
        ),
        migrations.RemoveField(
            model_name='park',
            name='notempat',
        ),
    ]