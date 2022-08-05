from django.contrib import admin
from .models import ToDo

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('creation_date', )

# Register your models here.
admin.site.register(ToDo, TodoAdmin)
