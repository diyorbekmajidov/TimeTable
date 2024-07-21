from django.contrib import admin
from .models import ClassRoom, Teacher, Science, ClassRoomScience
# from .forms import ClassRoomScienceForm
from .forms import TeacherAdminForm

class ClassRoomScienceInline(admin.TabularInline):
    model = ClassRoomScience
    # form = ClassRoomScienceForm
    extra = 1



class TeacherAdmin(admin.ModelAdmin):
    form = TeacherAdminForm
    list_display = ('fullname', 'description', 'date_create', 'date_update')



class ClassRoomAdmin(admin.ModelAdmin):
    inlines = [ClassRoomScienceInline]

admin.site.register(ClassRoom, ClassRoomAdmin)
admin.site.register(Science)
admin.site.register(Teacher, TeacherAdmin)
