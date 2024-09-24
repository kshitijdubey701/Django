from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import random
# Create your models here.
from django.core.validators import RegexValidator

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(
        max_length=15,   validators=[RegexValidator(r'^\+?1?\d{9,15}$')]  # Example: allows numbers like +12345678901
    ) # Ensure this matches the field name
    message = models.TextField()

    def __str__(self):
        return self.name

class LoginHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField(default=timezone.now)
    success = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {'Success' if self.success else 'Failed'}"
    
# myapp/models.py


class InternshipApplication(models.Model):
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('T', 'Trans'),
    ]
    
    InternshipApplication_time=models.DateTimeField(default=timezone.now)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    whatsapp_number = models.CharField(max_length=15)
    college_name = models.CharField(max_length=200)
    qualification = models.CharField(max_length=200)
    last_qualification_year = models.IntegerField()
    resume = models.FileField(upload_to='resumes/')  # Field to store uploaded resumes
    random_number = models.CharField(max_length=6, editable=False, unique=True)  # 6-digit random number

    def save(self, *args, **kwargs):
        if not self.random_number:  # Ensure it only generates a random number on the first save
            self.random_number = self.generate_random_number()
        super().save(*args, **kwargs)

    @staticmethod
    def generate_random_number():
        return str(random.randint(100000, 999999))  # Generates a 6-digit random number

    def __str__(self):
        return self.full_name
