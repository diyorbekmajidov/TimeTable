# Generated by Django 4.1.2 on 2024-07-21 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimeTable', '0003_teacher_day'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='day',
        ),
        migrations.AddField(
            model_name='teacher',
            name='workdays',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], default=1, max_length=255),
            preserve_default=False,
        ),
    ]
