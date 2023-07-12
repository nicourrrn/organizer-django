from django.contrib import admin
from api import models


admin.site.register(models.Note)
admin.site.register(models.NoteTag)
admin.site.register(models.NoteType)
admin.site.register(models.FinOperation)
admin.site.register(models.FinOperationTag)
admin.site.register(models.FinOperationType)
admin.site.register(models.Task)
admin.site.register(models.TaskStatus)
