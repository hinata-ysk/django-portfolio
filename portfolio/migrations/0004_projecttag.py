# Generated by Django 3.0.7 on 2020-08-02 08:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portfolio', '0003_auto_20200802_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='作成日時')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='更新日時')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Project')),
                ('tag', models.ForeignKey(default='ALL', on_delete=django.db.models.deletion.SET_DEFAULT, to='portfolio.Tag')),
            ],
        ),
    ]