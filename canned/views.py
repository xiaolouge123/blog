import json
import requests 

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

URL = 'http://localhost:8983/solr/gettingstarted/select?q={}'
query = 'book'
# Create your views here.

def index(request):

    # return HttpResponse('Hi bro!')
    return render(request, 'canned/index.html', {'answer': get_solr_response(query)} )

def get_solr_response(query):
    res = requests.get(URL.format(query), verify=False)
    txt = json.loads(res.text)
    return txt