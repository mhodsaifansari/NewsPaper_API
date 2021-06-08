from logging import error
from django.http.response import HttpResponse,JsonResponse
from django.shortcuts import render
#from . import webScrapper
import json
# Create your views here.
#from django_q.models import Schedule
object_data={}
from . import tasks

tasks.Collect_News(repeat=240)
def index(request):
    #return HttpResponse("Hello world")
    data_news=json.loads(get_data())
    
    return JsonResponse(get_data(),safe=False)

def get_data():
    f=open("testData.txt","r")
    #print(f.read())
    
    object_data=f.read()
    return object_data
    
    #        print("file not present")
    #        return {"data":"ERROR IN RETREVING DATA"}
