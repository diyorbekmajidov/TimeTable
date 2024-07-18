from django.contrib import admin
from .models import ClassRoom, Teacher, Science, ClassRoomScience
from .forms import ClassRoomScienceForm

class ClassRoomScienceInline(admin.TabularInline):
    model = ClassRoomScience
    form = ClassRoomScienceForm
    extra = 1

class ClassRoomAdmin(admin.ModelAdmin):
    inlines = [ClassRoomScienceInline]

admin.site.register(ClassRoom, ClassRoomAdmin)
admin.site.register(Teacher)
admin.site.register(Science)
