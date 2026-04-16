from django.contrib import admin
from  .models import Students
# Register your models here.
class StudentsAdmin(admin.ModelAdmin):
    list_display=("name","age","course")
    search_fields=('name','course')
    list_filter=('age',)
admin.site.register(Students,StudentsAdmin)