from django.shortcuts import redirect, render
from .forms import RegisterForm

# Create your views here.
def register(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("/index")
    return render(request, 'registration/register.html', {'form': form})

