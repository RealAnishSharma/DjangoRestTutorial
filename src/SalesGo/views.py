from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView


def logout_view(request):
    logout(request)
    return redirect('login')

def login_view(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            if request.GET.get('next'):
              return redirect(request.GET.get('next'))
            else:
             return redirect('home')
        else:
            error_message = 'Wrong Credentials. Try again'

    return render(request,'auth/login.html',{'error_message':error_message})


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class HomeView(TemplateView):
    template_name = "home.html"