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


# Hey Moses, do you understand the code you've written?
# Not reall ==> Ok
# the view you've written will be used for adding products and getting a list of products, hope you know that?
# Yeah ==> Ok
# So if that's case, we need a GET request for getting a list of products and POST for creating or adding a product? Hope you know that too?
# Yeah
# Okay so let's follow your code. when the view receives the request, your code checks if the request is a GET request or POST request
# If it is a GET request, then the block of code in the GET condition is what is going to run right? <== Are you with me ==> yeah
# Yeah
# okay. So the 1st line in the GET condition, product = Prryinoduct.objects.all(). You know what it's doing right?
# It's returns all objects <=== Products)  . So basically what you're trying to say is it returns all objects (products) from the 
# Product table in the db? ==> That's better pu. okay sot 
# So it should be products not product (better naming practice) since its many products
# okay. Great. 
# You understand what the next line (serializer) is doing ? ==> no. okay
# So basically when you pass a queryset into a serializer, like serializer = ProductSerializer(product, many=True).
# you need to simultaneously add the many parameter an
@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET': 
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(data=datetime(2000, 4, 5, 3, 23)) # serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
