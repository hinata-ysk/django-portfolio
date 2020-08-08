from django.shortcuts import (
    render,
    get_object_or_404,
    redirect
)
from .models import (
    Layout,
    AboutInfo,
    Tag,
    Portfolio,
    PortfolioTag,
    Project,
    ProjectTag
)

def index(request):
    layout = Layout.objects.filter(author=request.user).first()
    about_info = AboutInfo.objects.filter(author=request.user).first()
    tags = Tag.objects.filter(author=request.user).order_by('published_date')
    portfolios = Portfolio.objects.filter(author=request.user).order_by('published_date')
    portfolio_tags = PortfolioTag.objects.filter(author=request.user).order_by('published_date')
    projects = Project.objects.filter(author=request.user).order_by('published_date')
    project_tags = ProjectTag.objects.filter(author=request.user).order_by('published_date')

    if (not layout) or (not about_info):
        return redirect('accounts:logout')        

    portfolio_tag_maps = {}
    portfolio_pk_list = Portfolio.objects.filter(author__email='hinata.ysk@gmail.com').values_list('pk', flat=True).order_by('published_date')

    for portfolio_pk in list(portfolio_pk_list):
        portfolio_tag_pk_list = PortfolioTag.objects.filter(portfolio__pk=portfolio_pk).values_list('tag__pk', flat=True)
        tag_list = Tag.objects.filter(pk__in=list(portfolio_tag_pk_list)).values_list('tag', flat=True)
        portfolio_tag_maps[portfolio_pk] = ' '.join(list(tag_list))

    context = {
        'layout' : layout,
        'about_info' : about_info,
        'tags' : tags,
        'portfolios' : portfolios,
        'portfolio_tags' : portfolio_tags,
        'portfolio_tag_maps' : portfolio_tag_maps,
        'projects' : projects,
        'project_tags' : project_tags,
    }
    return render(request, 'portfolio/base.html', context)