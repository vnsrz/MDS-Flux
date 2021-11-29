from django.shortcuts import redirect, render
from .forms import RegisterForm

from django.contrib.auth import get_user_model
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .tokens import account_activation_token
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.contrib.auth.forms import PasswordResetForm
from django.db.models.query_utils import Q
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse

# Create your views here.


def register(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        email = form.cleaned_data.get('email')
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(request)
        mail_subject = 'Complete seu cadastro'
        message = render_to_string('registration/email_template.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        to_email = form.cleaned_data.get('email')
        send_mail(mail_subject, message, 'fluxwebapp@gmail.com', [to_email])
        header = "Confirme seu endereço de email"
        message = "Enviamos um e-mail de confirmação para sua conta, cheque sua caixa de entrada."
        return render(request, 'registration/confirm.html', {'header': header, 'message': message})
    return render(request, 'registration/register.html', {'form': form})


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        header = "Email confirmado com sucesso!"
        message = "Você já pode acessar sua conta no Flux."
        return render(request, 'registration/confirm.html', {'header': header, 'message': message})
    else:
        header = "Link de ativação inválido."
        message = "Ocorreu um erro inesperado na ativação da sua conta."
        return render(request, 'registration/confirm.html', {'header': header, 'message': message})

def password_reset_request(request):
    if request.method == "POST":
        User = get_user_model()
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Alteração de senha solicitada"
                    email_template_name = "password/password_email.html"
                    current_site = get_current_site(request)
                    c = {
                    'email':user.email,
                    'user': user,
                    'domain': current_site.domain,
                    'site_name': 'Website',
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
                    'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'fluxwebapp@gmail.com' , [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect ("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="password/password_reset.html", context={"password_reset_form":password_reset_form})