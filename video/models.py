from django.db import models
from accounts.models import Users

def upload_video_media(instance, filename):
    return "video/{0}/{1}".format(instance.uploaded_by.user.username, filename)
def upload_image_media(instance, filename):
    return "videoImage/{0}/{1}".format(instance.uploaded_by.user.username, filename)


class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField("GroupImage",upload_to=upload_image_media, null=True, blank=True)
    file = models.FileField("video",upload_to=upload_video_media)
    uploaded_by = models.ForeignKey(Users, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
    @property
    def profile_video(self):
        return self.file.url

    class Meta:
        verbose_name = "Videos"
        verbose_name_plural = "Videos"
        db_table = "Videos"
    