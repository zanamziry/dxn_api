from datetime import datetime
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from api.models import Agent, Product ,ServiceCenter
from api.serializers import AgentSerializer
from DXNAutopilot.DataCollector import Collector
from django.core.handlers.wsgi import WSGIRequest
# Create your views here.

@api_view(['POST'])
def inventory(request, id:str):
    """ Return a list of products available with Agents ID  //  
        specific Date Example: 'date=20-11-2022' to specify the date of the inventory list
    """
    date = None
    try:
        date = datetime.strptime(request.query_params['date'],"%d-%m-%Y")
    except Exception:
        date = datetime.now()
    try:
        ServiceCenter.objects.get(id=id)
    except Exception as s:
        return Response("Service Center Not Supported")
    c = Collector()
    serializer = AgentSerializer(data=request.data)
    if(serializer.is_valid()):
        if(c.Login(request.data['username'], request.data['password'])):
            jsonD:dict = c.GetInventoryReport(id ,DateOfReport=date)
            return Response(jsonD)
        else:
            return Response("invalid username or password")
    else:
        Response("invalid data")

@api_view(['GET'])
def getAllCenters(request:Request):
    """ Get A List Of Agents Available """
    ag_list = ServiceCenter.objects.all().values('id','name').order_by('id')
    return Response(ag_list)

@api_view(['GET'])
def getProducts(request:Request):
    """ Get A List Of Products """
    pr_list = Product.objects.all().order_by('id')
    return Response(pr_list.values())

@api_view(['POST'])
def TestLogin(request):
    """ If User and Password are right the result is True Else False """
    serializer = AgentSerializer(data=request.data)
    if(serializer.is_valid()):
        c = Collector()
        return Response(c.Login(request.data['username'],request.data['password']))
    else:
        return Response(False)