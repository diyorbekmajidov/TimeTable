from django.db import models
from django.utils.translation import gettext_lazy as _

class Science(models.Model):
    name = models.CharField(max_length=45, blank=False, verbose_name=_('name'))
    is_group = models.BooleanField(default=False, blank=True, verbose_name=_('is_group'))
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('description'))
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    VERBOSE_NAME = _('Science')

    def __str__(self) -> str:
        return self.name
    
from django.db import models

class Teacher(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    ]

    fullname = models.CharField(max_length=60, verbose_name=_('fullname'))
    sciences = models.ManyToManyField('Science', related_name="teachers", verbose_name=_('sciences'))
    workdays = models.CharField(max_length=255, verbose_name=_('workdays'))  # Store as a comma-separated string
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('description'))
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    VERBOSE_NAME = _('Teacher')

    def __str__(self) -> str:
        return self.fullname

    def get_workdays(self):
        return self.workdays.split(',')


class ClassRoom(models.Model):
    # sinf qo'shish va unga birdan fanlar birik terish
    SEMINA_CHOICES = [
        ('1', "Tushlikgacha"),
        ('2', "Tushlikdan so'ng")
    ]

    name = models.CharField(max_length=45, verbose_name=_('name'))
    semina = models.CharField(max_length=50, choices=SEMINA_CHOICES, verbose_name=_('semina'))
    leader = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    # sciences = models.ManyToManyField(Science, through='ClassRoomScience', related_name="classes")
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('description'))
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    VERBOSE_NAME = _('ClassRoom')

    def __str__(self) -> str:
        return self.name
    

class ClassRoomScience(models.Model):
    # yaratilgan sinfga fan birik terish va usha fanaga o'qtuvchi ham berikterish
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, verbose_name=_('classroom'))
    science = models.ForeignKey(Science, on_delete=models.CASCADE, verbose_name=_('science'))
    times_per_week = models.PositiveIntegerField(verbose_name=_('times_per_week'))
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name=_('teacher'))
    teacher2 = models.ForeignKey(Teacher, null=True, blank=True, on_delete=models.SET_NULL, related_name='teacher2', verbose_name=_('teacher2'))
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    VERBOSE_NAME = _('ClassRoomScience')

    class Meta:
        unique_together = ('classroom', 'science')

    def __str__(self) -> str:
        return f"{self.classroom.name} - {self.science.name} ({self.times_per_week} marta)"