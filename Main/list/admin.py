from django.contrib import admin
from .models import CompletedGeneration

class CompletedGenerationAdmin(admin.ModelAdmin):
    list_display = ('uid', 'name', 'course', 'duration', 'email', 'generation_time', 'certificate')

admin.site.register(CompletedGeneration, CompletedGenerationAdmin)
