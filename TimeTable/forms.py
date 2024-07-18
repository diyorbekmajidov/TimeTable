from django import forms
from .models import ClassRoomScience, Teacher

class ClassRoomScienceForm(forms.ModelForm):
    class Meta:
        model = ClassRoomScience
        fields = ['science', 'teacher', 'times_per_week']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'science' in self.data:
            try:
                science_id = int(self.data.get('science'))
                self.fields['teacher'].queryset = Teacher.objects.filter(sciences__id=science_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty teacher queryset
        elif self.instance.pk:
            self.fields['teacher'].queryset = self.instance.science.teachers
        else:
            self.fields['teacher'].queryset = Teacher.objects.none()

    def clean(self):
        cleaned_data = super().clean()
        science = cleaned_data.get('science')
        teacher = cleaned_data.get('teacher')

        if science and teacher and not teacher.sciences.filter(id=science.id).exists():
            self.add_error('teacher', f'Teacher {teacher.fullname} does not teach {science.name}')
        
        return cleaned_data
