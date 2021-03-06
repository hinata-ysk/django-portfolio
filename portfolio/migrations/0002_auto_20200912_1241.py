# Generated by Django 3.0.7 on 2020-09-12 03:41

from django.conf import settings
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioimage',
            name='display_sort',
            field=models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='portfolioimage',
            unique_together={('author', 'portfolio', 'display_sort')},
        ),
        migrations.RemoveField(
            model_name='portfolioimage',
            name='display_order',
        ),
    ]
