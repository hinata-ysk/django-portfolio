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
    ProjectTag,
    Skill,
    SkillLevel
)

import plotly.express as px
from plotly.offline import plot
import plotly.graph_objects as go
import pandas as pd
from django_pandas.io import read_frame

def index(request):
    layout = Layout.objects.filter(author=request.user).first()
    about_info = AboutInfo.objects.filter(author=request.user).first()
    tags = Tag.objects.filter(author=request.user).order_by('published_date')
    portfolios = Portfolio.objects.filter(author=request.user).order_by('published_date')
    portfolio_tags = PortfolioTag.objects.filter(author=request.user).order_by('published_date')
    projects = Project.objects.filter(author=request.user).order_by('published_date')
    project_tags = ProjectTag.objects.filter(author=request.user).order_by('published_date')
    skills = Skill.objects.filter(author=request.user).order_by('published_date')
    skill_levels = SkillLevel.objects.all().order_by('level')

    if (not layout) or (not about_info):
        return redirect('accounts:logout')        

    portfolio_tag_maps = {}
    portfolio_pk_list = Portfolio.objects.filter(author__email='hinata.ysk@gmail.com').values_list('pk', flat=True).order_by('published_date')

    for portfolio_pk in list(portfolio_pk_list):
        portfolio_tag_pk_list = PortfolioTag.objects.filter(portfolio__pk=portfolio_pk).values_list('tag__pk', flat=True)
        tag_list = Tag.objects.filter(pk__in=list(portfolio_tag_pk_list)).values_list('tag', flat=True)
        portfolio_tag_maps[portfolio_pk] = ' '.join(list(tag_list))

    skill_charts = []
    for classification in skills.values_list('classification').order_by('classification').distinct():
        df = read_frame(skills.filter(classification=classification), fieldnames=['skill_name', 'level', 'level__level'])
        fig = go.Figure(go.Scatterpolar(
            name = classification[0],
            r = df['level__level'],
            theta = df['skill_name'],
            opacity=1,#不透明度
            mode='lines+markers',
            text=df['level'],
            hoverinfo='theta+text'
            ))
        fig.update_traces(fill='toself')
        fig.update_layout(template='plotly_dark')
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            polar = dict(
                radialaxis = dict(range=[0, 5], showticklabels=True,tickfont=dict(size=15)),
                angularaxis = dict(showticklabels=True,tickfont=dict(size=20))
            ),
            # title={
            #     'text': "Plot Title",
            #     'y':0.9,
            #     'x':0.5,
            #     'xanchor': 'center',
            #     'yanchor': 'top'}
            title=dict(text='<b>{0}</b>'.format(classification[0]), y=0.9, x=0.5, xanchor='center', yanchor='bottom'),
            font=dict(size=25)
        )
        chart_html = plot(fig, config={'displayModeBar':False}, output_type='div', include_plotlyjs=False)
        skill_charts.append(chart_html)


    context = {
        'layout' : layout,
        'about_info' : about_info,
        'tags' : tags,
        'portfolios' : portfolios,
        'portfolio_tags' : portfolio_tags,
        'portfolio_tag_maps' : portfolio_tag_maps,
        'projects' : projects,
        'skill_levels' : skill_levels,
        'project_tags' : project_tags,
        'skill_charts' : skill_charts,
    }
    return render(request, 'portfolio/base.html', context)

def test(request):
    return render(request, 'portfolio/test.html')      
