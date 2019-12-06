from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Hi bro!')
    # return render(request, 'canned/index.html', {'answer': get_solr_response(1)} )

def get_solr_response(query):
    return 'Hi bro!'