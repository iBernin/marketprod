from django.contrib.auth.decorators import login_required
# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

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

# @login_required
class MonitorIdsListView(LoginRequiredMixin, ListView):
    model = MonitorIds
    # form_class = MonitorIdsForm


class MonitorIdsDetailView(DetailView):
    model = MonitorIds
