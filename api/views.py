from datetime import datetime
import json
from django.http import HttpResponse, JsonResponse
from api.models import Agent
from DXNAutopilot.DataCollector import Collector
from django.core.handlers.wsgi import WSGIRequest
#{"id":"141100033", "username":"duhok", "password":"zxcv1010"}
# Create your views here.

def inventory(request:WSGIRequest, id:str):
    #jsonb = json.loads(request.body.decode('utf-8'))
    print(request.query_params)
    agent = Agent.objects.get(id=id)
    c = Collector(agent.id, agent.username, agent.password)
    date = datetime.strptime(date,"%d-%m-%Y")
    jsonD:dict = c.GetInventoryReport(DateOfReport=date)
    return JsonResponse(jsonD)

def getAgentInfo(request:WSGIRequest, id):
    t = Agent.objects.get(id=id)
    return HttpResponse(t.id)

def getAllAgents(request:WSGIRequest):
    t = Agent.objects.all()
    jsonObj = {'list' : []}
    for i in t:
        a = {
        'id' : i.id,
        'username' : i.username,
        }
        jsonObj['list'].append(a)
    return JsonResponse(jsonObj)