from django.shortcuts import render

def home(request):
    return render(request, 'end2/index.html')
