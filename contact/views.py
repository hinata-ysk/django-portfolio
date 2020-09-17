from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import ContactForm
from portfolio.models import AboutInfo

# Create your views here.

class ContactFormView(FormView):
    template_name = 'contact/contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:contact_result')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        name = self.kwargs.get('name')
        about_info = AboutInfo.objects.filter(author__name=name).first()

        context["about_info"] = about_info
        return context

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class ContactResultView(TemplateView):
    template_name = 'contact/contact_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success'] = "お問い合わせは正常に送信されました。"
        return context