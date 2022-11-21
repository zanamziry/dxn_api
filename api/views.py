from datetime import datetime
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from api.models import Agent, Product
from DXNAutopilot.DataCollector import Collector
from django.core.handlers.wsgi import WSGIRequest
#{"id":"141100033", "username":"duhok", "password":"zxcv1010"}
# Create your views here.

@api_view(['GET'])
def inventory(request:Request, id:str):
    """ Return a list of products available with Agents ID  //  
        specific Date Example: 'date=20-11-2022' to specify the date of the inventory list
    """
    date = None
    try:
        date = datetime.strptime(request.query_params['date'],"%d-%m-%Y")
    except Exception:
        date = datetime.now()
    agent = Agent.objects.get(id=id)
    c = Collector(agent.id, agent.username, agent.password)
    jsonD:dict = c.GetInventoryReport(DateOfReport=date)
    return Response(jsonD)

@api_view(['GET'])
def getAgentInfo(request:Request, id):
    """ This Is A Test """
    t = Agent.objects.get(id=id)
    return Response(t.jsonSerializable())

@api_view(['GET'])
def getAllAgents(request:Request):
    """ Get A List Of Agents Available """
    ag_list = Agent.objects.all().values('id','username')
    return Response(ag_list)

@api_view(['GET'])
def getProducts(request:Request):
    """ Get A List Of Products """
    pr_list = Product.objects.all()
    return Response(pr_list.values())