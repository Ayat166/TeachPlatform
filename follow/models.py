from django.db import models
from accounts.models import Users

# Create your models here.
class Follow (models.Model):
    following = models.ForeignKey(Users, on_delete=models.CASCADE,related_name="following_users",
        null=True,
        blank=True,)
    followed = models.ForeignKey(Users, on_delete=models.CASCADE,related_name="followed_users",
        null=True,
        blank=True,)
    followed_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.following}:{self.followed}"
    
    
    class Meta:
        verbose_name = "Follow"
        verbose_name_plural = "Follow"
        db_table = "Follow"