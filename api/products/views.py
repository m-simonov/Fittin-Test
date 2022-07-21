from os.path import dirname

from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Product

from . import serializers


class ProductListView(APIView):
    def post(self, request):
        categories = request.data.get('category')
        price_start = request.data.get('price_start', 0)
        price_end = request.data.get('price_end', 1000000)
        if not categories:
            return Response(
                data={"Field 'category' is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        if price_start and price_end:
            products = (
                Product.objects
                .prefetch_related('category')
                .filter(
                    category__in=categories,
                    price__gte=price_start,
                    price__lte=price_end
                )
            )
        else:
            products = (
                Product.objects
                .prefetch_related('category')
                .filter(
                    category__in=categories,
                )
            )
        serialized = serializers.ProductListSerializer(products, many=True)
        return Response(serialized.data)


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.prefetch_related('category', 'offers')
    serializer_class = serializers.ProductSerializer


class FileUploadView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        file = request.FILES['file']
        if file.content_type != "application/xml":
            return Response(
                data="The file must be in 'xml' format",
                status=status.HTTP_400_BAD_REQUEST
            )
        opened_file = open(dirname(__file__) +
                           f'/management/commands/feed/{file.name}', 'wb+')
        for chunk in file.chunks():
            opened_file.write(chunk)
        opened_file.close()
        return Response(status=status.HTTP_201_CREATED)
