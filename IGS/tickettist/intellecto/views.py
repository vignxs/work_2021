from curses.ascii import HT
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

def home(request):
    return render(request,"intellecto/home.html")


def tickettist(request):
    form = UserForm()

    if  request.method == 'POST':
        print(request.POST)
        # form = UserForm(request.POST)
        # if form.is_valid():
        #     form.save()

    context={'form' : form}
    return render(request,"intellecto/main.html",context)

