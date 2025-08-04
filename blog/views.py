from django.shortcuts import render

def index_fronti(request):
    return render(request, 'index.html')

def login_list(request):
    return render(request, 'login.html')  # login.html - siz yuborgan HTML
