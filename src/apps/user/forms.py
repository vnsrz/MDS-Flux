from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    username = forms.CharField(label = "Nome de usuário", min_length=4, max_length=150)
    email = forms.EmailField(label = "Email", max_length=75)
    
    class Meta:
	    model = CustomUser
	    fields = ('username', 'email')

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            user = CustomUser.objects.get(email=email)
            raise forms.ValidationError("Email já cadastrado")
        except CustomUser.DoesNotExist:
            return email

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"]
        user.is_active = True 
        if commit:
            user.save()
        return user