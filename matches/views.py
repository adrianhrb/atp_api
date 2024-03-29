import requests
import codecs

from django.shortcuts import render
from prettyconf import config
from django.views.decorators.csrf import csrf_exempt

from .utils import build_custom_prompt
from .forms import MatchAI

@csrf_exempt
def form_ai(request):
    if request.method == 'POST':
        form = MatchAI(data=request.POST)
        if form.is_valid():
            url = config('URL')
            payload = {
                'model': config('MODEL'),
                'messages': [{'role': 'user', 'content': build_custom_prompt(form.cleaned_data['match'])}],
                'temperature': 0.7,
                'max_tokens': 200
            }
            headers = {
                'Content-Type': 'application/json',
            }
            r = requests.request('POST', url=url, json=payload, headers=headers)        
            response = r.json()
            #response = simulated_reponse(data)
            generated_text = response['choices'][0]['message']['content']
            return render(request, 'ai_result.html', dict(text=generated_text))
    else:
        form = MatchAI()
        return render(request, 'ai.html', dict(form=form))

def simulated_reponse(data):
    if data['model'] == config('MODEL') and data['rol'] == 'user':
        response = {
            'choices': [
                {
                    'finish_reason': 'length',
                    'index': 0,
                    'message': {
                        'content': "El partido fue bien",
                        'role': 'assistant'
                    },
                    'references': []
                }
            ],
            'created': 170612544,
            'id': 'foobar',
            'model': 'minimal',
            'object': 'text',
            'ussage':{
                'completion_tokens': 100,
                'prompt_tokens': 35,
                'total_tokens': 135
            }
        }
        return response