# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response

def searchview(request):
    return render_to_response('searchapp/searchPage.html')
