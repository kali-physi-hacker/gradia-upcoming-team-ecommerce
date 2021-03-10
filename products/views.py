from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response





def test_view(request):
    """
    This is to demonstrate views in django
    return:
    """
    template = "index.html"
    context = {}
    return render(request=request, template_name=template, context=context)



# gets a single product 
@api_view(['GET'])
def get_singleproduct() :
    """
        this to show we can get a single product 

    """
    return Response({"message": "Hello for today! See you tomorrow!"}) 
