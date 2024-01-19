from django.shortcuts import render
from .models import MonitorIds
from django.views.generic import ListView, DetailView
# from .forms import MonitorIdsForm



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
    # form_class = MonitorIdsForm


class MonitorIdsDetailView(DetailView):
    model = MonitorIds