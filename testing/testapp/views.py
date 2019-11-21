from django.http import HttpResponse
from django.shortcuts import render
from datetime import *
import dateutil.parser
import requests
import json
from github import Github


def index(request):
    context = requests.get('https://api.github.com/organizations')
    final_result = []
    output = json.loads(context.text)
    org_id = int(request.GET.get('org'))
    for todo in output:
       if (todo['id'] == org_id):
            content = requests.get(todo['repos_url']+'?sort=stargazers_count&direction=desc')
    result = json.loads(content.text)
    for test in result:
       value = json.dumps({
        "name": test['name'],
        "stars": test['stargazers_count']
        }, sort_keys=True, indent=4)
       final_result.append(value)
    
    return HttpResponse((final_result))

    
   

