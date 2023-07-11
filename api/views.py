from rest_framework import generics, viewsets
from api import serializers, models

class TaskView(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer


# Додати можливість діставати таски за статусом
class TaskStatusView(viewsets.ModelViewSet):
    queryset = models.TaskStatus.objects.all()
    serializer_class = serializers.TaskStatusSerializer
