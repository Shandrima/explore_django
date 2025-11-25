from django.db import models 
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.core.exceptions import ValidationError




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
        ('cyber security', 'CYBER SECURITY'),
        ('ai', 'AI'),
        ('btech','BTECH'),
        ('bcom','BCOM'),

    ]


    name = models.CharField(max_length=100,
        validators=[RegexValidator(r'^[A-Za-z ]+$', "Only letters allowed")]
    )
    age = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(120)]
    )

    course = models.CharField(max_length=100, choices=COURSE_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='male')
    is_active = models.BooleanField(default=True)
    joining_date = models.DateField(auto_now_add=True) 

    def __str__(self):
        return self.name
    
class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    SUBJECT_CHOICES = [
    ('maths', 'Maths'),
    ('science', 'Science'),
    ('english', 'English'),
    ('python','Python'),
    ('java','Java'),
]

    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)

    score = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )


    def __str__(self):
       return f"{self.subject} - {self.score}"


    

    
    



