from django import forms
from django.contrib import admin
from .models import Teacher

class TeacherAdminForm(forms.ModelForm):
    workdays = forms.MultipleChoiceField(
        choices=Teacher.DAY_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Teacher
        fields = ['fullname', 'sciences', 'workdays', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['workdays'].initial = self.instance.get_workdays()

    def save(self, commit=True):
        teacher = super().save(commit=False)
        teacher.workdays = ','.join(self.cleaned_data['workdays'])
        if commit:
            teacher.save()
            self.save_m2m()
        return teacher
    

from django import forms
from .models import Teacher

class TeacherForm(forms.ModelForm):
    workdays = forms.MultipleChoiceField(
        choices=Teacher.DAY_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Teacher
        fields = ['fullname', 'sciences', 'workdays', 'description']

    def save(self, commit=True):
        teacher = super().save(commit=False)
        teacher.workdays = ','.join(self.cleaned_data['workdays'])
        if commit:
            teacher.save()
            self.save_m2m()
        return teacher

