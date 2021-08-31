from django.urls import path

from .views import *


urlpatterns = [
    path('', samp_response)
]