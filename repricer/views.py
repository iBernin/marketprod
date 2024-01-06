from django.shortcuts import render
from . models import MonitorIds

def repricer_view(request):
    nmIds = MonitorIds.objects.all()
    context = {
        'MonitorIds': nmIds
    }
    return render(request, 'repricer/index.html', context)