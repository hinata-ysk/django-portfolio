# Generated by Django 3.0.7 on 2020-08-10 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20200804_0826'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutinfo',
            name='top_image',
            field=models.ImageField(default='def.png', upload_to='portfolio/about_info', verbose_name='Top画像'),
        ),
    ]