from django.db import models
from django.core.validators import RegexValidator
from uuid import uuid4
from PIL import Image
import re

# REGEX
regNo_regex = RegexValidator(
regex="^[A-Z]{3}/[A-Z]{3}/[0-9]{2}/?[0-9]{5}$",
message="Registration Number entered was not correctly formated!!",
)

phone_regex = RegexValidator(
regex = "^\+?1?\d{10,13}$",
message="Phone number entered was not correctly formated!!",
)

# Create your models here.

class Course(models.Model):
    code = models.CharField(max_length = 10, unique = True)
    name = models.CharField(max_length = 100, unique = True)

    class Meta:
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.name + ' ' +'(' + self.code + ')'


# def students_pics(instance, filename):
#     ext = filename.split('.')[1]
#     new_filename = '{}.{}'.format(uuid4(), ext)
#     return f'students_pics/{instance.user_id}/{new_filename}'


class Student(models.Model):
    fname = models.CharField(max_length = 20)
    sname = models.CharField(max_length = 20, blank = True)
    lname = models.CharField(max_length = 20)
    regno = models.CharField( validators = [regNo_regex], max_length = 30, unique = True )
    course = models.ForeignKey(Course, models.SET_NULL, blank = True, null = True)
    year = models.PositiveIntegerField()
    email = models.EmailField(null = True, blank = True)
    phoneNumber = models.CharField( validators = [phone_regex], max_length=15)
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

def test_videos(instance, filename):
    ext = filename.split('.')[1]
    new_filename = '{}.{}'.format(uuid4(), ext)
    return f'test_videos/{instance.id}/{new_filename}'


class TestVideo(models.Model):
    video = models.FileField(upload_to = test_videos)

    def __str__(self):
        return str(self.video)
