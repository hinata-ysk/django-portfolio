# Generated by Django 3.0.7 on 2020-09-06 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0021_auto_20200901_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutinfo',
            name='sns_card_image',
            field=models.ImageField(default='def_top_image.png', upload_to='portfolio/about_info/sns_card', verbose_name='SNS Card Image'),
        ),
        migrations.AlterField(
            model_name='aboutinfo',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='問い合わせ用メールアドレス'),
        ),
        migrations.AlterField(
            model_name='aboutinfo',
            name='github',
            field=models.CharField(help_text='アカウント名はプロフィールが表示される"https://github.com/{アカウント名}"のアカウント名', max_length=100, verbose_name='GitHub アカウント名'),
        ),
        migrations.AlterField(
            model_name='aboutinfo',
            name='twitter',
            field=models.CharField(help_text='ユーザー名は@の後ろに続く英数字', max_length=50, verbose_name='Twitter ユーザ名'),
        ),
        migrations.AlterField(
            model_name='portfolioimage',
            name='display_order',
            field=models.IntegerField(choices=[(1, 'First'), (2, 'Second'), (3, 'Therd')]),
        ),
    ]
