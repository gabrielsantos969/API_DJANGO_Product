import json
from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from products.models import Product


from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProtuctSerializer

@api_view(["POST"])
def api_home(request, *args, **kwargs):

    serializer = ProtuctSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        
        #instance = serializer.save()
        print(serializer.data)
        return JsonResponse(serializer.data)

    return Response({"invalid": "Not good data"}, status=400)



@api_view(["GET"])
def easter_egg(request, *args, **kwargs):

    data = {
        'welcome': 'Bem vindo a API com Django',
        'author': 'Gabriel Santos',
        'start': '19/12/2022',
        'last_update': '21/12/2022'
        }

    return Response(data, status=200) 
   