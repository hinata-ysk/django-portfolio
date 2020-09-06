from django.shortcuts import (
    render,
    get_object_or_404,
    redirect
)
from .models import (
    AboutInfo, 
    Tag,
    Portfolio,
    PortfolioImage,
    PortfolioTag,
    Project,
    ProjectTag,
    Skill,
    SkillLevel,
)

import plotly.express as px
from plotly.offline import plot
import plotly.graph_objects as go
from django_pandas.io import read_frame

def PortfolioView(request,name):
    about_info = AboutInfo.objects.filter(author__name=name).first()
    tags = Tag.objects.filter(author__name=name).order_by('published_date')
    portfolios = Portfolio.objects.filter(author__name=name).order_by('-published_date')
    portfolio_images = PortfolioImage.objects.filter(author__name=name)
    portfolio_tags = PortfolioTag.objects.filter(author__name=name).order_by('published_date')
    projects = Project.objects.filter(author__name=name).order_by('-published_date')
    project_tags = ProjectTag.objects.filter(author__name=name).order_by('published_date')
    skills = Skill.objects.filter(author__name=name).order_by('published_date')
    skill_levels = SkillLevel.objects.all().order_by('level')

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
            title=dict(text='<b>{0}</b>'.format(classification[0]), y=0.9, x=0.5, xanchor='center', yanchor='bottom'),
            font=dict(size=25)
        )
        chart_html = plot(fig, config={'displayModeBar':False}, output_type='div', include_plotlyjs=False)
        skill_charts.append(chart_html)


    context = {
        'about_info' : about_info,
        'tags' : tags,
        'portfolios' : portfolios,
        'portfolio_images' : portfolio_images,
        'portfolio_tags' : portfolio_tags,
        'projects' : projects,
        'skill_levels' : skill_levels,
        'project_tags' : project_tags,
        'skill_charts' : skill_charts,
    }
    return render(request, 'portfolio/portfolio.html', context)

def test(request):
    return render(request, 'portfolio/test.html')      
