from rest_framework import generics, viewsets
from api import serializers, models

class TaskView(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer


# Додати можливість діставати таски за статусом
class TaskStatusView(viewsets.ModelViewSet):
    queryset = models.TaskStatus.objects.all()
    serializer_class = serializers.TaskStatusSerializer


class NoteView(viewsets.ModelViewSet):
    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer


class NoteTagView(viewsets.ModelViewSet):
    queryset = models.NoteTag.objects.all()
    serializer_class = serializers.NoteTagSerializer

class NoteTypeView(viewsets.ModelViewSet):
    queryset = models.NoteType.objects.all()
    serializer_class = serializers.NoteTypeSerializer

class FinOperationView(viewsets.ModelViewSet):
    queryset = models.FinOperation.objects.all()
    serializer_class = serializers.FinOperationSerializer


class FinOperationPresetView(viewsets.ModelViewSet):
    queryset = models.FinOperationPreset.objects.all()
    serializer_class = serializers.FinOperationPresetSerializer


class FinOperationTagView(viewsets.ModelViewSet):
    queryset = models.FinOperationTag.objects.all()
    serializer_class = serializers.FinOperationTagSerializer


class FinOperationTypeView(viewsets.ModelViewSet):
    queryset = models.FinOperationPreset.objects.all()
    serializer_class = serializers.FinOperationTypeSerializer


