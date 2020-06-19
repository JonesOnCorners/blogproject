from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user         = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name   = models.CharField(max_length=100,default="")
    middle_name  = models.CharField(blank=True, null=True, max_length=100)
    last_name    = models.CharField(max_length=100,default="")
    phone_number = models.CharField(max_length=20, blank=False, null=False, default="")
    address      = models.TextField(default="")
    profile_pic = models.ImageField(default="media/images/profile_pics/default.jpg",upload_to='media/images/profile_pics/')

    def __str__(self):
        return f"{self.user.username} profile"
