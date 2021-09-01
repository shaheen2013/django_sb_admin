from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.views import View

from user.forms.form import LoginForm


class Login(View):
    def get(self, request):
        form = LoginForm()
        context = {'form': form, }
        return render(request, 'login.html', context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            try:
                auth.authenticate(form.cleaned_data)
            except:
                print('hello')
        print('aa')
        return redirect('/user/login')
