import requests

from django.shortcuts import render
from prettyconf import config
from .forms import MatchAI

def form_ai(request):
    if request.method == 'POST':
        form = MatchAI(data=request.POST)
    else:
        form = MatchAI()
        return render(request, 'ai.html', dict(form=form))

def process_request(request, )