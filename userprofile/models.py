from django.db import models

# Create your models here.


class UserProfile_model(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.PositiveBigIntegerField()
    gender = models.CharField(max_length=10, choices=[
                              ['Male', 'Male'], ['Female', 'Female']])
    age = models.PositiveIntegerField()
    desc = models.TextField(max_length=500)
    profile_picture = models.ImageField(upload_to='profile_pics/')
    profile_resume = models.FileField(upload_to='profile_resume/')
