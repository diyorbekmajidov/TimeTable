# Generated by Django 4.1.2 on 2024-07-31 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TimeTable', '0009_alter_teacher_workdays'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroomscience',
            name='teacher2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher2', to='TimeTable.teacher'),
        ),
    ]
