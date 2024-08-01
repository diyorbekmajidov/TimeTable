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

    class Media:
        js = (
            "js/group.js",
            "https://code.jquery.com/jquery-3.3.1.min.js",
        )

admin.site.register(ClassRoom, ClassRoomAdmin)
admin.site.register(Science)
admin.site.register(Teacher, TeacherAdmin)
