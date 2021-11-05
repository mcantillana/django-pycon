from django.shortcuts import render

def home(request):
    template_name = 'home.html'
    data = {}

    return render(request, template_name, data)