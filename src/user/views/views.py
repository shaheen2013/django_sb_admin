from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import View


class User(View):
    def get(self, request):
        return render(request, 'index.html')
