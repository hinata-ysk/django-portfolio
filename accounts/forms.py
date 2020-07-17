from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()
YEAR = timezone.now().year

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #htmlの表示を変更可能にします
        # self.fields['email'].widget.attrs['class'] = 'form-control'
        # self.fields['date_of_birth'].widget.attrs['class'] = 'form-control'
        # self.fields['password1'].widget.attrs['class'] = 'form-control'
        # self.fields['password2'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        # fields = '__all__'
        fields = ("email", 'date_of_birth', "password1", "password2",)
        widgets = {
            'date_of_birth': forms.SelectDateWidget(years=[x for x in range(YEAR - 70, YEAR + 1)])
        }

class UserUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #htmlの表示を変更可能にします
        # self.fields['email'].widget.attrs['class'] = 'form-control'
        # self.fields['date_of_birth'].widget.attrs['class'] = 'form-control'
        # self.fields['password1'].widget.attrs['class'] = 'form-control'
        # self.fields['password2'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        # fields = '__all__'
        fields = ('date_of_birth', "password1", "password2",)
        widgets = {
            'date_of_birth': forms.SelectDateWidget(years=[x for x in range(YEAR - 70, YEAR + 1)])
        }
