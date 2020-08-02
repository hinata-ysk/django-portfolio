from django.db import models
from django.utils import timezone
from django.conf import settings

class Project(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project_name = models.CharField(verbose_name='プロジェクト名' ,max_length=200)
    term_from = models.DateTimeField(verbose_name='参画期間(自)')
    term_to = models.DateTimeField(verbose_name='参画期間(至)', blank=True, null=True)
    created_date = models.DateTimeField(verbose_name='作成日', default=timezone.now)
    published_date = models.DateTimeField(verbose_name='更新日', blank=True, null=True)

    def publish(self):
        self.published_date =timezone.now()
        self.save()

    def __str__(self):
        return '{0} | {1} ~ {2}'.format(self.project_name, self.term_from.strftime('%Y/%m/%d'), self.term_to.strftime('%Y/%m/%d'))
