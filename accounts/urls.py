from django.urls import path
from . import views

app_name ='accounts'

urlpatterns =[
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('create/', views.CreateAccount.as_view(), name='create_account'),
    path('<int:pk>/update/', views.UpdateAccount.as_view(), name='update_account'),
]