from django.shortcuts import render
from django.views.generic import CreateView
from users.forms import MpUserCreateForm
from users.models import MpUser


class MpUserCreateView(CreateView):
    model = MpUser
    success_url = '/'
    form_class = MpUserCreateForm
    # template_name =


def logout_confirm(request):
    return render(request, 'registration/logout.html')
