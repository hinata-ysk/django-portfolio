from django.urls import path
from . import views

app_name = 'portfolio'

# urlpatterns = [
#     path('portfolio/',views.portfolio, name='portfilio'),
#     path('portfolio/<int:pk>/', views.portfolio_detail, name='portfolio_detail'),
#     path('portfolio/new/', views.portfolio_new, name='portfolio_new'),
#     path('portfolio/<int:pk>/edit', views.portfolio_edit, name='portfolio_edit'),
#     path('portfolio/<int:pk>/remove', views.portfolio_remove, name='portfolio_remove'),
# ]

urlpatterns = [
    path('<name>',views.PortfolioView, name='portfolio'),
]