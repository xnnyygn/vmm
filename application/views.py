from django.shortcuts import render

def create(request):
    return render(request, 'application/create.html')
