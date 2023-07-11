from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from api import models, forms

class ClientUserAdmin(UserAdmin):
    add_form = forms.ClientCreationForm
    form = forms.ClientChangeForm
    model = models.Client
    list_display = ['username']

admin.site.register(models.Note)
admin.site.register(models.NoteTag)
admin.site.register(models.NoteType)
admin.site.register(models.FinOperation)
admin.site.register(models.FinOperationTag)
admin.site.register(models.FinOperationType)
admin.site.register(models.Task)
admin.site.register(models.TaskStatus)
admin.site.register(models.Client, ClientUserAdmin)
