from django.contrib.auth.forms import UserChangeForm, UserCreationForm 
from api import models 

class ClientCreationForm(UserCreationForm):
    class Meta:
        model = models.Client
        fields = ('username', )


class ClientChangeForm(UserChangeForm):
    class Meta:
        model = models.Client
        fields = ('username', 'main_task')
