from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserOptions(models.TextChoices):
    Teacher = "Teacher", "Teacher"
    Student = "Student", "Student"

def upload_profile_image_media(instance, filename):
    return "profile_image/{0}/{1}".format(instance.user.username, filename)

class Users (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_options = models.CharField(
        "user-options", choices=UserOptions.choices, max_length=7, null=True, default=None
    )
    first_name = models.CharField(
        verbose_name="first name", max_length=20, null=True, blank=True
    )
    last_name = models.CharField(
        verbose_name="last name", max_length=20, null=True, blank=True
    )
    profile_image = models.ImageField(
        "profile mage", null=True, upload_to=upload_profile_image_media, blank=True
    )
    def __str__(self):
        return self.user.username
    
    @property
    def profile_img(self):
        return self.profile_image.url

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        db_table = "users"
