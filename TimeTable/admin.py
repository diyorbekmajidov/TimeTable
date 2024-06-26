from django.contrib import admin
from .models import Science, Teacher, ClassRoom, ClassRoomScience

class ClassRoomScienceInline(admin.TabularInline):
    model = ClassRoomScience
    extra = 1

class ClassRoomAdmin(admin.ModelAdmin):
    inlines = [ClassRoomScienceInline]

admin.site.register(Science)
admin.site.register(Teacher)
admin.site.register(ClassRoom, ClassRoomAdmin)
