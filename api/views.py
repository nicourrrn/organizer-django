import io

from rest_framework import viewsets, parsers, renderers
from rest_framework.permissions import IsAuthenticated
from api import serializers, models, permissions

class TaskView(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
    permission_classes = [IsAuthenticated, permissions.IsTaskOwner]

    def get_queryset(self):
        return self.queryset.filter(owner = self.request.user)

    def create(self, request, *args, **kwargs):
        data = parsers.JSONParser().parse(io.BytesIO(request.body))
        data['owner'] = request.user.id
        request.body = renderers.JSONRenderer().render(data)
        return super().create(request, *args, **kwargs)
    

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


