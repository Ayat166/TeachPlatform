from django.db import models
from video.models import Video
from accounts.models import Users

def upload_video_media(instance, filename):
    return "GroupImage/{0}/{1}".format(instance.user.user.username, filename)

class Group(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField("GroupImage",upload_to=upload_video_media, null=True, blank=True)
    videos = models.ManyToManyField(Video, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Group"
        db_table = "Group"