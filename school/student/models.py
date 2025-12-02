from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    yearOfstudy = models.IntegerField()
    course = models.CharField(max_length=200)

    def __str__(self):
        return f'Student {self.name} course {self.course}'
    