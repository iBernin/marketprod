from django.contrib.auth.models import User, AbstractUser
from django.db import models


class MpUser(AbstractUser):
    pass
    # date_joined = None
    email = models.EmailField('email address', unique=True)
    # # avatar = models.ImageField(upload_to='avatars', blank=True)
    # b_year = models.PositiveIntegerField(null=True)