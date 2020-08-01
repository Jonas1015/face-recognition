from django.db import models
from PIL import Image

# Create your models here.

class Course(models.Model):
    code = models.CharField(max_length = 10, unique = True)
    name = models.CharField(max_length = 100, unique = True)

    class Meta:
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.name + ' ' +'(' + self.code + ')'




class Student(models.Model):
    fname = models.CharField(max_length = 20)
    sname = models.CharField(max_length = 20, blank = True)
    lname = models.CharField(max_length = 20)
    regno = models.CharField(max_length = 30, unique = True )
    course = models.ForeignKey(Course, models.SET_NULL, blank = True, null = True)
    year = models.PositiveIntegerField()
    phoneNumber = models.PositiveIntegerField()
    image = models.ImageField(upload_to = 'student_pics')


    class Meta:
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.fname + " " + self.sname + " " + self.lname

    def save(self, force_insert = False, force_update = False, using=None):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 1000 or img.width > 1000:
            output_size = (1000,1000)
            img.thumbnail(output_size)
            img.save(self.image.path)
