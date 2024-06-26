from django.db import models

class Science(models.Model):
    name = models.CharField(max_length=45, blank=False)
    description = models.CharField(max_length=255, blank=True, null=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

class Teacher(models.Model):
    fullname = models.CharField(max_length=60)
    sciences = models.ManyToManyField(Science, related_name="teachers")
    description = models.CharField(max_length=255, blank=True, null=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.fullname

class ClassRoom(models.Model):
    SEMINA_CHOICES = [
        ('1', "Tushlikgacha"),
        ('2', "Tushlikdan so'ng")
    ]

    name = models.CharField(max_length=45)
    semina = models.CharField(max_length=50, choices=SEMINA_CHOICES)
    leader = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    sciences = models.ManyToManyField(Science, through='ClassRoomScience', related_name="classes")
    description = models.CharField(max_length=255, blank=True, null=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    

class ClassRoomScience(models.Model):
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    science = models.ForeignKey(Science, on_delete=models.CASCADE)
    times_per_week = models.PositiveIntegerField()

    class Meta:
        unique_together = ('classroom', 'science')

    def __str__(self) -> str:
        return f"{self.classroom.name} - {self.science.name} ({self.times_per_week} marta)"