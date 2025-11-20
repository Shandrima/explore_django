from django.db import models


# Create your models here.

class Student(models.Model):

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    COURSE_CHOICES = [
        ('bca', 'BCA'),
        ('computer science', 'COMPUTER SCIENCE'),
        ('data science', 'DATA SCIENCE'),
        ('cyber sequrity', 'CYBER SEQURITY'),
        ('ai', 'AI'),
        ('btech','BTECH'),
        ('bcom','BCOM'),

    ]


    name = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.CharField(max_length=100, choices=COURSE_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='male')
    is_active = models.BooleanField(default=True)
    joining_date = models.DateField(auto_now_add=True) 

    def __str__(self):
        return self.name
    
class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    score = models.IntegerField()

    
    



