from django.contrib import admin
from api.models import Student, Word, Dict

class StudentAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'war_name', 'number']

class WordAdmin(admin.ModelAdmin):
    fields = ['gender', 'word', 'translation']

class DictAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'words']

admin.site.register(Student, StudentAdmin)
admin.site.register(Word, WordAdmin)
admin.site.register(Dict, DictAdmin)
