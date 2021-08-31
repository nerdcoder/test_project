from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def samp_response(request):
    app = ({'app_name' : "test app"})
    return JsonResponse(app)