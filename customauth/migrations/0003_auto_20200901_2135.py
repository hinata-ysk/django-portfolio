# Generated by Django 3.0.7 on 2020-09-01 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customauth', '0002_myuser_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='avater',
            field=models.ImageField(blank=True, null=True, upload_to='customauth'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='favicon',
            field=models.ImageField(blank=True, null=True, upload_to='customauth'),
        ),
    ]
