from django.contrib import messages
from django.contrib.auth import hashers
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

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # try:
            #     user = User.objects.get(username=username)
            #     if user:
            #         check_user = user.check_password(password)
            #         if check_user:
            #             auth.login(request, user)
            #             messages.info(request, 'login success')
            #             return redirect('/user')
            # except:
            #     messages.error(request, 'Invalid username')
            #     return redirect('/user/login')
            # messages.error(request, 'Invalid Password')
            # return redirect('/user/login')

            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.info(request, 'login success')
                return redirect('/user')
        messages.error(request, 'Invalid credentials')
        return redirect('/user/login')
