import requests
import json

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# 固定请求，返回一条数据，查询接口好像设置还有问题
# URL = 'https://content-eval-test-solr-searchenginedemo-dev.usspk05.app.apple.com/solr/canned/select?q=*%3A*&rows=1&start=1'
URL = 'http://localhost:8983/solr/gettingstarted/select?q=*:*'
query = "*:*"

def index(request):
    # return HttpResponse('Hi bro!')
    return render(request, 'canned/index.html', {'answer': get_solr_response(query)} )

def get_solr_response(query):
    res = requests.get(URL.format(query), verify=False)
    # response_result = json.loads(res.text)
    # return response_result['response']['docs'][0]['type'][0]
    return str(res.text)


    