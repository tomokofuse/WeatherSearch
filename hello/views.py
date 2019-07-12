from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView
import re
from datetime import datetime
from django.http import HttpResponse
from django.db.models import Q
from hello.models import Tenki

def search(request):
    search_area = request.GET.get('search_area')
    
    if search_area is None or search_area == "":
        search_area = ""
        context = {'tenkis': Tenki.objects.all().filter(area=search_area)}
    else:
        context = {'tenkis': Tenki.objects.all().filter(
            Q(area__contains=search_area) |
            Q(prefecture__contains=search_area)
        )}

    return render(request,"hello/search.html",context=context)