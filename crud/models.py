from django.db import models

class ClassRoom(models.Model):
    name=models.CharField(max_length=20,)

    def __str__(self):
        return self.name


class Student(models.Model):
    classroom=models.ForeignKey(ClassRoom, on_delete=models.CASCADE,null=True, blank=True)
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    email=models.EmailField(max_length=20)
    address=models.CharField(max_length=50)

    def __str__(self):
        return f"Student.{self.name}"

class StudentProfile(models.Model):
    student=models.OneToOneField(Student, on_delete=models.CASCADE)
    phone=models.CharField(max_length=14)
    bio=models.TextField(max_length=500)
    profile_picture=models.FileField(null=True, blank=True)

    def __str__(self):
        return f"Profile of {self.student.name}"
