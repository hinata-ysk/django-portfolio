from django.contrib import admin
from .models import (
    Layout,
    AboutInfo,
    Tag,
    Portfolio,
    PortfolioTag,
    Project,
    ProjectTag,
    Skill,
    SkillLevel,
    SkillClass,
)

admin.site.register(Layout)
admin.site.register(AboutInfo)
admin.site.register(Tag)
admin.site.register(Portfolio)
admin.site.register(PortfolioTag)
admin.site.register(Project)
admin.site.register(ProjectTag)
admin.site.register(Skill)
admin.site.register(SkillLevel)
admin.site.register(SkillClass)

