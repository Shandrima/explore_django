from django.contrib import admin

# Register your models here.
from .models import Student, Mark

admin.site.site_header = "My Student Portal"
admin.site.index_title = "Welcome to Student Admin Panel"


class MarkInline(admin.TabularInline):   
    model = Mark
    extra = 1  

@admin.action(description="Make selected students Active")
def make_students_active(modeladmin, request, queryset):
    queryset.update(is_active=True)

@admin.action(description="Make selected students Inactive")
def make_students_inactive(modeladmin, request, queryset):
    queryset.update(is_active=False)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age", "course","gender","joining_date","is_active")
    list_per_page = 5
    list_filter = ("course", "is_active")
    search_fields = ("name", "course")
    list_editable = ("course", "is_active")
    ordering = ("name",)
    actions = [make_students_active, make_students_inactive]


    inlines = [MarkInline]

    fieldsets = (
        ("Personal Info", {"fields": ("name", "age", "gender")}),
        ("Academic Info", {"fields": ("course","is_active")}),  
    )

    def get_readonly_fields(self, request, obj=None):
    
        if obj and not obj.is_active:
            return ("joining_date", "age")  # both are read-only
    
        return ()
    

