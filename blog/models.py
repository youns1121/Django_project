from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    contentDetail = models.TextField(null=True, default='')

    #auth : Foreign key(외래키)로 나중에 셋팅
    created_at = models.DateTimeField(auto_now_add=True) # 자동으로 날짜 입력
    updated_at = models.DateTimeField(auto_now=True) # 자동으로 날짜 입력

    def __str__(self):
        return f'[{self.pk}]{self.title}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}'

