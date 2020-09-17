from django import forms
from django.conf import settings
from django.core.mail import BadHeaderError, EmailMessage
from django.http import HttpResponse


class ContactForm(forms.Form):
    name = forms.CharField(
        label='お名前',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        }),
    )
    email = forms.EmailField(
        label='メールアドレス',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
        }),
    )
    message = forms.CharField(
        label='お問い合わせ内容',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
        }),
    )

    def send_email(self):
        subject = "Portfolio Contact Form"
        message = self.cleaned_data['message']
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        from_email = email
        to_email = [email]
        bcc_email = [settings.EMAIL_HOST_USER]
        try:
            # send_mail(subject, message, from_email, recipient_list)
            msg = EmailMessage(subject,message,from_email,to_email,bcc_email)
            msg.send()
        except BadHeaderError:
            return HttpResponse("無効なヘッダが検出されました。")