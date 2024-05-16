from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Voca(models.Model):
    number_vo=models.IntegerField()
    english_vo=models.CharField(max_length=100)#길이 100까지
    korean_vo=models.CharField(max_length=100)#길이 100까지
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_voca')
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_voca')  # 추천인 추가

    def __str__(self):
        return self.english_vo
    

class Comment(models.Model):
    voca=models.ForeignKey(Voca, on_delete=models.CASCADE)
    content= models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.content