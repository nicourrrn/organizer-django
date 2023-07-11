from django.contrib import admin
from api import models

admin.register(models.Note)
admin.register(models.NoteTag)
admin.register(models.NoteType)
admin.register(models.FinOperation)
admin.register(models.FinOperationTag)
admin.register(models.FinOperationType)
admin.register(models.Task)
admin.register(models.TaskStatus)
