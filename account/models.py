from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

 

class CustomUser(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=100,unique=True)
    email = models.EmailField(unique=True)
    user_bio = models.CharField(max_length=50)
    user_profile_image =models.ImageField(upload_to='profile')
    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = UserManager() #-----------------------------> create object
    def __str__(self):
        return self.email
    
    
class Author(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
    
    
class Course(models.Model):
    name = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,related_name='course')
    
    def __str__(self):
        return self.name
    