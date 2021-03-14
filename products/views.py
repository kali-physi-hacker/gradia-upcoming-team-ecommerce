from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

from datetime import datetime


def test_view(request):
    """
    This is to demonstrate views in django
    return:
    """
    template = "index.html"
    context = {}
    return render(request=request, template_name=template, context=context)


@api_view(["GET", "POST"])
def product_list(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# gets a single product
@api_view(["GET", "DELETE", "PUT"])
def product_detail(request, pk):
    """
    Gets a single product
    :param request:
    :param pk:
    returns:
    """
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(data={"error": "Product does not exist"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ProductSerializer(product)
        return Response(data={"product": serializer.data}, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = ProductSerializer(instance=product, data=request.data)
        if not serializer.is_valid():
            return Response(data={"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()

        return Response(data={"product": serializer.data}, status=status.HTTP_201_CREATED)

    elif request.method == "DELETE":
        serializer = ProductSerializer(instance=product, data={"is_active": False})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data={"message": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
