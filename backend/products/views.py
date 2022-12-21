from rest_framework import generics

from .models import Product
from .serializers import ProtuctSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProtuctSerializer

product_detail_view = ProductDetailAPIView.as_view()