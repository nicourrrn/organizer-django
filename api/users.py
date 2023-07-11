from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import UserChangeForm, UserCreationForm 
from django.db import models

from api import models as api_models

class ClientCreationForm(UserCreationForm):
    class Meta:
        model = api_models.Client
        fields = ('username', )


class ClientChangeForm(UserChangeForm):
    class Meta:
        model = api_models.Client
        fields = ('username', 'main_task')
