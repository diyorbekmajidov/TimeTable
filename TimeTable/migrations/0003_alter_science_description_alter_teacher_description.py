# Generated by Django 4.1.2 on 2024-06-25 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimeTable', '0002_alter_teacher_science'),
    ]

    operations = [
        migrations.AlterField(
            model_name='science',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
