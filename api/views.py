from datetime import datetime
import json
from django.http import HttpResponse, JsonResponse
from api.models import Agents
from DXNAutopilot.DataCollector import Collector
from django.core.handlers.wsgi import WSGIRequest
#{"id":"141100033", "username":"duhok", "password":"zxcv1010"}
# Create your views here.
def inventory(request:WSGIRequest, id:str, date:str=datetime.strftime(datetime.now(),'%d-%m-%Y')):
    #jsonb = json.loads(request.body.decode('utf-8'))
    agent = Agents.objects.get(id=id)
    c = Collector(agent.id, agent.username, agent.password)
    date = datetime.strptime(date,"%d-%m-%Y")
    jsonD:dict = c.GetInventoryReport(DateOfReport=date)
    return JsonResponse(jsonD)

def addAgent(request:WSGIRequest):
    data = json.loads(request.body)
    agent = Agents(id=data['id'], username=data['username'], password=data['password'])
    agent.save()
    return HttpResponse(f'Successfully Added {agent.username}')

def deleteAgent(request:WSGIRequest):
    data = json.loads(request.body)
    agent = Agents.objects.get(id=data['id'])
    if(agent.username == data['username'] and agent.password == data['password']):
        agent.delete()
    return HttpResponse(f'Successfully Removed {agent.username}')

def getAgentInfo(request:WSGIRequest, id):
    t = Agents.objects.get(id=id)
    return HttpResponse(t.id)