from django.db import models
from django.utils import timezone
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

class AboutInfo(models.Model):
    author = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='タイトル', max_length=100)
    email = models.EmailField(verbose_name='問い合わせ用メールアドレス')
    main_text = models.CharField(verbose_name='メインテキスト', default='', blank=True, max_length=100)
    sub_text = models.TextField(verbose_name='サブテキスト', default='', blank=True, max_length=200)
    top_image = models.ImageField(verbose_name='Top画像' , upload_to='portfolio/about_info/top', default='def_top_image.png')
    avater = models.ImageField(verbose_name='アイコン画像' , upload_to='portfolio/about_info', default='def_icon.png')
    favicon = models.ImageField(verbose_name='アイコン画像(favicon)' , upload_to='portfolio/about_info', default='def_favicon.png')
    description = models.TextField(verbose_name='説明文', max_length=400)
    website = models.URLField(verbose_name='ウェブサイト', max_length=200)
    twitter = models.CharField(verbose_name='Twitter ユーザ名', max_length=50, help_text='ユーザー名は@の後ろに続く英数字')
    github = models.CharField(verbose_name='GitHub アカウント名', max_length=100, help_text='アカウント名はプロフィールが表示される"https://github.com/{アカウント名}"のアカウント名')
    sns_card_image = models.ImageField(verbose_name="SNS Card Image", upload_to='portfolio/about_info/sns_card', default='def_top_image.png')
    created_date = models.DateTimeField(verbose_name='作成日時', default=timezone.now, editable=False)
    published_date = models.DateTimeField(verbose_name='更新日時', blank=True, null=True)

    def __str__(self):
        return self.author.get_short_name()

class Tag(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tag = models.CharField(verbose_name='ポートフォリオタグ', max_length=50, blank=False, null=False)
    created_date = models.DateTimeField(verbose_name='作成日時', default=timezone.now, editable=False)
    published_date = models.DateTimeField(verbose_name='更新日時', blank=True, null=True)

    def __str__(self):
        return self.tag

class Portfolio(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='タイトル', max_length=100, blank=False, null=False)
    thumbnail_image = models.ImageField(verbose_name='イメージ画像' , upload_to='portfolio/portfolioImage', blank=True, null=True)
    discription = models.TextField(verbose_name='解説', max_length=500, blank=True, null=False)
    github_url = models.URLField(verbose_name='GitHub URL', max_length=200, blank=True, null=False)
    demo_url = models.URLField(verbose_name='Demo URL', max_length=200, blank=True, null=False)
    created_date = models.DateTimeField(verbose_name='作成日時', default=timezone.now, editable=False)
    published_date = models.DateTimeField(verbose_name='更新日時', blank=True, null=True)

    def publish(self):
        self.published_date =timezone.now()
        self.save()

    def __str__(self):
        return self.title

class PortfolioImage(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    display_sort = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    image = models.ImageField(verbose_name='イメージ画像' , upload_to='portfolio/portfolioImage', blank=True, null=True)
    created_date = models.DateTimeField(verbose_name='作成日時', default=timezone.now, editable=False)
    published_date = models.DateTimeField(verbose_name='更新日時', blank=True, null=True)

    class Meta:
        unique_together=(('author','portfolio','display_sort'))

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return "{0}:{1}".format(self.portfolio.title, self.display_sort)

class PortfolioTag(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.SET_DEFAULT, default='ALL')
    created_date = models.DateTimeField(verbose_name='作成日時', default=timezone.now, editable=False)
    published_date = models.DateTimeField(verbose_name='更新日時', blank=True, null=True)

    def __str__(self):
        return '{0}:{1}'.format(self.portfolio.title, self.tag)        

class Project(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project_name = models.CharField(verbose_name='プロジェクト名' ,max_length=200)
    term_from = models.DateTimeField(verbose_name='参画期間(自)')
    term_to = models.DateTimeField(verbose_name='参画期間(至)', blank=True, null=True)
    role = models.CharField(verbose_name='役割', max_length=200, blank=True, null=True)
    process = models.CharField(verbose_name='参画工程', max_length=200, blank=True, null=True)
    overview = models.TextField(verbose_name='プロジェクト概要', max_length=400, blank=True, null=True)
    created_date = models.DateTimeField(verbose_name='作成日時', default=timezone.now, editable=False)
    published_date = models.DateTimeField(verbose_name='更新日時', blank=True, null=True)

    def publish(self):
        self.published_date =timezone.now()
        self.save()

    def __str__(self):
        return '{0} | {1} ~ {2}'.format(self.project_name, self.term_from.strftime('%Y/%m/%d'), self.term_to.strftime('%Y/%m/%d'))

class ProjectTag(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.SET_DEFAULT, default='ALL')
    created_date = models.DateTimeField(verbose_name='作成日時', default=timezone.now, editable=False)
    published_date = models.DateTimeField(verbose_name='更新日時', blank=True, null=True)

    def __str__(self):
        return '{0}:{1}'.format(self.project.project_name, self.tag)

class SkillClass(models.Model):
    classification = models.CharField(max_length=10, primary_key=True)
    created_date = models.DateTimeField(verbose_name='作成日時', default=timezone.now, editable=False)
    published_date = models.DateTimeField(verbose_name='更新日時', blank=True, null=True)
    
    def __str__(self):
        return self.classification

class SkillLevel(models.Model):
    level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],primary_key=True)
    level_text = models.CharField(max_length=50)
    created_date = models.DateTimeField(verbose_name='作成日時', default=timezone.now, editable=False)
    published_date = models.DateTimeField(verbose_name='更新日時', blank=True, null=True)

    def __str__(self):
        return self.level_text

class Skill(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    classification = models.ForeignKey(SkillClass, on_delete=models.CASCADE)
    skill_name = models.CharField(verbose_name='スキル名', max_length=100)
    level = models.ForeignKey(SkillLevel, on_delete=models.CASCADE)
    created_date = models.DateTimeField(verbose_name='作成日時', default=timezone.now, editable=False)
    published_date = models.DateTimeField(verbose_name='更新日時', blank=True, null=True)

    def __str__(self):
        return self.skill_name

