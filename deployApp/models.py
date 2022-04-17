from django.db import models

# Create your models here.
class Student(models.Model):
    rollNo = models.IntegerField(default=0)
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.rollNo) + " " + self.name