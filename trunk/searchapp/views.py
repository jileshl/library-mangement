# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from models import Library, Type
from django.template import RequestContext

import logging

logger = logging.getLogger(__name__)

def searchview(request):
    return render_to_response('searchapp/searchPage.html')

def searchresult(request):
    if request.method == 'POST':
        c = {}
        c.update(csrf(request))
        searchtxt = request.POST['search']
        searchOption = request.POST['searchfield']
        
        librarys = []
        if ('0' == searchOption):
            librarys = searchAll(searchtxt)
            
        elif ('1' == searchOption):
            librarys = searchParticulars(searchtxt)

        elif  ('2' == searchOption):
            librarys = searchProject(searchtxt)        

        elif ('3' == searchOption):
            librarys = searchIssue(searchtxt)

        elif ('4' == searchOption):
            librarys = searchEvent(searchtxt)

        elif ('5' == searchOption):
            librarys = searchGeneral(searchtxt)

        else:
            librarys = searchNotparticulars(searchtxt)


        type2libmap = {}

        for library in librarys:
            if not type2libmap.has_key(library.type):
                type2libmap[library.type]=[]
                
            type2libmap[library.type].append(library)

        print type2libmap
        return render_to_response('searchapp/searchPage.html', {'search': request.POST['search'],
                                                                'searchfield': request.POST['searchfield'],
                                                                'searchResult': 'true',
                                                                'searchResultValue':type2libmap},
                                  context_instance=RequestContext(request))

def searchAll(value):
    result = []
    result.extend(searchParticulars(value))
    result.extend(searchNotparticulars(value))
    return result

def searchParticulars(value):
    return Library.objects.filter(particulars__icontains=value).order_by('year')

def searchProject(value):
    return Library.objects.filter(project__shortname__icontains=value).order_by('year')

def searchIssue(value):
    return Library.objects.filter(issue__icontains=value).order_by('year')

def searchEvent(value):
    return Library.objects.filter(event__icontains=value).order_by('year')

def searchGeneral(value):
    return Library.objects.filter(general__icontains=value).order_by('year')

def searchNotparticulars(value):
    result = []
    result.extend(searchProject(value))
    result.extend(searchIssue(value))
    result.extend(searchEvent(value))
    result.extend(searchGeneral(value))

    return result
    


