from django.shortcuts import render


def test_view(request):
    """
    This is to demonstrate views in django
    return:
    """
    template = "index.html"
    context = {}
    return render(request=request, template_name=template, context=context)
