from django.db import models

# Create your models here.

 class  book (models.Model) :
    name = models.CharField(max_length=200)  # 书名
    writer = models.CharField(max_length=100)  # 作者


