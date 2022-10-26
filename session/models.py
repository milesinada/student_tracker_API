from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=64)
    cohort = models.CharField(max_length=64)
    email = models.EmailField(max_length=60)

    def __str__(self):
        return self.name

class Session(models.Model):
    FOLLOWUP = 'followup'
    RESOLVED = 'resolved'

    STATUS_CHOICES =(
        (FOLLOWUP, 'Follow Up'),
        (RESOLVED, 'Resolved')
    )
    issue = models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    duration = models.CharField(max_length=32)
    unit = models.CharField(max_length=32)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=FOLLOWUP)
    student = models.ForeignKey(Student, related_name='students', on_delete=models.CASCADE)
    def __str__(self):
        return self.issue