from django.contrib import admin

# Register your models here.
from .models import Student, Mark


class MarkInline(admin.TabularInline):   
    model = Mark
    extra = 1  

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age", "course","gender","is_active")
    list_filter = ("course", "is_active")
    search_fields = ("name", "course")
    inlines = [MarkInline]

    def get_readonly_fields(self, request, obj=None):
        if obj and not obj.is_active:
            return ("age",)
        return ()
