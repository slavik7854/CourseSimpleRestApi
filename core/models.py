from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    age = models.PositiveSmallIntegerField()
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return '{} {}'.format(self.last_name, self.first_name)


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)
    members = models.ManyToManyField(Student, through='Membership')

    def __str__(self):
        return self.title


class Membership(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{}, {}'.format(self.course, self.student)
