from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

def index(request):
    if request.session['logado']:
        return render(request, 'index.html')
    else:
        return redirect('/auth/login/?status=2')
