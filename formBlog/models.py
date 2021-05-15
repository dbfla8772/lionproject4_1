from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Blog(models.Model):
    objects = models.Manager()

    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'formBlog/', blank=True, null=True) 
    image_thumbnail = ImageSpecField(source = 'image',processors=[ResizeToFill(120,100)])

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100] 