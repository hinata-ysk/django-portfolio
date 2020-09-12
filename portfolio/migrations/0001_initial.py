# Generated by Django 3.0.7 on 2020-09-06 03:09

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='タイトル')),
                ('thumbnail_image', models.ImageField(blank=True, null=True, upload_to='portfolio/portfolioImage', verbose_name='イメージ画像')),
                ('discription', models.TextField(blank=True, max_length=500, verbose_name='解説')),
                ('github_url', models.URLField(blank=True, verbose_name='GitHub URL')),
                ('demo_url', models.URLField(blank=True, verbose_name='Demo URL')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='作成日時')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='更新日時')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=200, verbose_name='プロジェクト名')),
                ('term_from', models.DateTimeField(verbose_name='参画期間(自)')),
                ('term_to', models.DateTimeField(blank=True, null=True, verbose_name='参画期間(至)')),
                ('role', models.CharField(blank=True, max_length=200, null=True, verbose_name='役割')),
                ('process', models.CharField(blank=True, max_length=200, null=True, verbose_name='参画工程')),
                ('overview', models.TextField(blank=True, max_length=400, null=True, verbose_name='プロジェクト概要')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='作成日時')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='更新日時')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SkillClass',
            fields=[
                ('classification', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='作成日時')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='更新日時')),
            ],
        ),
        migrations.CreateModel(
            name='SkillLevel',
            fields=[
                ('level', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('level_text', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='作成日時')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='更新日時')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50, verbose_name='ポートフォリオタグ')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='作成日時')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='更新日時')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=100, verbose_name='スキル名')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='作成日時')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='更新日時')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('classification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.SkillClass')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.SkillLevel')),
            ],
        ),
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
        migrations.CreateModel(
            name='PortfolioTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='作成日時')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='更新日時')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Portfolio')),
                ('tag', models.ForeignKey(default='ALL', on_delete=django.db.models.deletion.SET_DEFAULT, to='portfolio.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='AboutInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='タイトル')),
                ('email', models.EmailField(max_length=254, verbose_name='問い合わせ用メールアドレス')),
                ('main_text', models.CharField(blank=True, default='', max_length=100, verbose_name='メインテキスト')),
                ('sub_text', models.TextField(blank=True, default='', max_length=200, verbose_name='サブテキスト')),
                ('top_image', models.ImageField(default='def_top_image.png', upload_to='portfolio/about_info/top', verbose_name='Top画像')),
                ('avater', models.ImageField(default='def_icon.png', upload_to='portfolio/about_info', verbose_name='アイコン画像')),
                ('favicon', models.ImageField(default='def_favicon.png', upload_to='portfolio/about_info', verbose_name='アイコン画像(favicon)')),
                ('description', models.TextField(max_length=400, verbose_name='説明文')),
                ('website', models.URLField(verbose_name='ウェブサイト')),
                ('twitter', models.CharField(help_text='ユーザー名は@の後ろに続く英数字', max_length=50, verbose_name='Twitter ユーザ名')),
                ('github', models.CharField(help_text='アカウント名はプロフィールが表示される"https://github.com/{アカウント名}"のアカウント名', max_length=100, verbose_name='GitHub アカウント名')),
                ('sns_card_image', models.ImageField(default='def_top_image.png', upload_to='portfolio/about_info/sns_card', verbose_name='SNS Card Image')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='作成日時')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='更新日時')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_order', models.IntegerField(choices=[(1, 'First'), (2, 'Second'), (3, 'Therd')])),
                ('image', models.ImageField(blank=True, null=True, upload_to='portfolio/portfolioImage', verbose_name='イメージ画像')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='作成日時')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='更新日時')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Portfolio')),
            ],
            options={
                'unique_together': {('author', 'portfolio', 'display_order')},
            },
        ),
    ]
