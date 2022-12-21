import json
from django.forms import model_to_dict
# from django.http import JsonResponse, HttpResponse
from products.models import Product

from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProtuctSerializer

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data= model_to_dict(instance, fields=['id', 'title', 'price'])
        data = ProtuctSerializer(instance).data
    return Response(data)
   