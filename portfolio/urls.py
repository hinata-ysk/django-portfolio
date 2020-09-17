from django.urls import path
from . import views 

app_name = 'portfolio'

urlpatterns = [
    path('<name>',views.PortfolioView, name='portfolio'),
]