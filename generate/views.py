from django.shortcuts import render
import random

def home(request):
    return render(request,'generate/home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = request.GET.get('length',8)
    if request.GET.get('all'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        characters.extend(list('1234567890'))
        characters.extend(list('!@#%&*?/'))
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('num'):
        characters.extend(list('1234567890'))
    if request.GET.get('specialchar'):
        characters.extend(list('!@#%&*?/'))
    passwd = ''
    for i in range(int(length)):
        passwd +=random.choice(characters)
    return render(request,'generate/password.html',{'passwd':passwd})


def about(request):
    return render(request,'generate/about.html')

