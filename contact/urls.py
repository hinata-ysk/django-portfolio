from django.urls import path
from . import views 

app_name = 'contact'

urlpatterns = [
    path('form/<name>',views.ContactFormView.as_view(), name='contact_form'),
    path('result',views.ContactResultView.as_view(), name='contact_result'),
]