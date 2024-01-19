from django.contrib.auth.forms import UserCreationForm
from users.models import MpUser


class MpUserCreateForm(UserCreationForm):
    class Meta:
        model = MpUser
        fields = ('username', 'email', 'password1', 'password2')
