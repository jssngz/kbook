from django.db import models

# Create your models here.

class   Book(models.Model):
    # 书名
    name = models.CharField(max_length=200)
    # 作者
    writer = models.CharField(max_length=100)

    def __str__(self):
        return self.name +','+self.writer



