from django.db import models

# Create your models here.
class Blog(models.Model):
    objects = models.Manager()

    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'formBlog/', blank=True, null=True) # upload_to는 업로드할 폴더를 지정하는 것, 사진 이름이 저장, MEDIA_URL로 지정해둔 media 폴더 안에 blog 폴더 생성하서 관리

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100] 