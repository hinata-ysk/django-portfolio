# Generated by Django 3.0.7 on 2020-08-22 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_auto_20200822_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='overview',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='プロジェクト概要'),
        ),
    ]
