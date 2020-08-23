# Generated by Django 3.0.7 on 2020-08-13 00:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_auto_20200812_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='作成日時'),
        ),
        migrations.AddField(
            model_name='skill',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='更新日時'),
        ),
    ]
