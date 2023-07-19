from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=32)
    lastName = models.CharField(max_length=32)
    image = models.ImageField(default='media/profile.jpg',upload_to='media')

    def __str__(self):
        return self.firstName, self.lastName,self.image