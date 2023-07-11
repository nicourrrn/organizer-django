from rest_framework import serializers
from api import models

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.User
        fields = "__all__"

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Task
        fields = "__all__"

class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TaskStatus
        fields = "__all__"


class FinOperationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.FinOperation
        fields = "__all__"

class FinOperationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FinOperationType
        fields = "__all__"

class FinOperationTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FinOperationTag
        fields = "__all__"

class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Note
        fields = "__all__"

class NoteTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NoteType
        fields = "__all__"


class NoteTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NoteTag
        fields = "__all__"


