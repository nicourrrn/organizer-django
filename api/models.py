from django.db import models
from django.contrib.auth.models import User


class TaskStatus(models.Model):
    name = models.CharField(max_length=16)

class Task(models.Model):
    name = models.CharField(max_length=64)
    content = models.TextField()
    status = models.ForeignKey(TaskStatus, on_delete=models.SET_NULL, null=True)
    parent = models.ForeignKey("Task", on_delete=models.CASCADE, null=True)
    

class AppUser(User):
    main_task = models.ForeignKey(Task, on_delete=models.CASCADE) 
   
class FinOperationType(models.Model):
    name = models.CharField(max_length=64)

class FinOperationTag(models.Model):
    name = models.CharField(max_length=32)

class FinOperation(models.Model):
    operation_type = models.ForeignKey(FinOperationType, on_delete=models.SET_NULL,
                                       null=True)
    date = models.DateTimeField(auto_now=True)
    desctiption = models.CharField(max_length=64)
    tags = models.ManyToManyField(FinOperationTag)


class FinOperationPreset(models.Model):
    name = models.CharField(max_length=64)
    reference = models.ForeignKey(FinOperation, on_delete=models.CASCADE)

class NoteType(models.Model):
    name = models.CharField(max_length=64)

class NoteTag(models.Model):
    name = models.CharField(max_length=32)

class Note(models.Model):

    class NoteEvaluation(models.IntegerChoices):
        Worst  = 0
        Worse  = 1
        Bad    = 2
        Normal = 3 
        Better = 4
        Best   = 5

    name = models.CharField(max_length=64, default='') 
    content = models.TextField()
    date = models.DateTimeField(auto_now=True)
    evaluation = models.IntegerField(choices=NoteEvaluation.choices)
    tags = models.ForeignKey(NoteTag, on_delete=models.CASCADE) 
    note_type = models.ForeignKey(NoteType, on_delete=models.SET_NULL, null=True)
     

