from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer
# Create your views here.


class ListViewsProduct(APIView):

    def get(self , request):
        products = Product.objects.all()
        ser_data = ProductSerializer(instance=products , many=True)
        return Response(data = ser_data.data)



class CreateViewProduct(APIView):

    def post(self , request):
        ser_data = ProductSerializer(data = request.data)

        if ser_data.is_valid(raise_exception=True):
            ser_data.save()
            return Response({'massage':'Your blog was created'} , status=201)

        else:
            return Response(ser_data.errors , status=404)



class UpdateViewProduct(APIView):

    def put(self , request , product_id):
        product  = Product.objects.get(id = product_id)
        ser_data = ProductSerializer(instance=product , data = request.data)
        if ser_data.is_valid():
            ser_data.save()
            return Response({'masage':'Your product was updated'} , status=200)

        else:
            return Response(ser_data.errors , status=404)




class DeleteViewProduct(APIView):

    def delete(self , request , product_id):
        product = Product.objects.get(id = product_id)
        product.delete()
        product.save()
        return Response({'massage':'Your product was deleted'})