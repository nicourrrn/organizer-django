from rest_framework import serializers
from api import models

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Task
        fields = "__all__"


