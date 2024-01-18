from django.shortcuts import render
from .models import MonitorIds
from django.views.generic import ListView, DetailView


# def repricer_view(request):
#     nmIds = MonitorIds.objects.all()
#     context = {
#         'MonitorIds': nmIds
#     }
#     return render(
#         request,
#         'repricer/index.html',
#         context,
#     )

class MonitorIdsListView(ListView):
    model = MonitorIds


class MonitorIdsDetailView(DetailView):
    model = MonitorIds