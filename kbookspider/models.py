from django.db import models

# Create your models here.

class Kbook (models.Model):
    kkdBookId = models.IntegerField() #kkd 书籍id
    bookName = models.CharField(max_length=100) #书籍名称
    clickNum = models.IntegerField() #点击数量
    doubanImgSrc = models.CharField(max_length=1000) #豆瓣图片地址
    doubanBookUrl = models.CharField(max_length=1000) #豆瓣图书地址
    tag = models.ManyToManyField('Tag') #标签列表
    writer = models.ForeignKey('Writer') #作者
    bookType = models.ForeignKey('BookType')  # 分类

    #京东的1是产品特色
    detail_tag_id_2 = models.CharField(max_length=100000)  # 编辑推荐
    detail_tag_id_3 = models.CharField(max_length=100000) # 内容简介
    detail_tag_id_4 = models.CharField(max_length=100000)  # 作者简介
    detail_tag_id_5 = models.CharField(max_length=100000)  # 精彩书评
    detail_tag_id_6 = models.CharField(max_length=100000) # 目录
    detail_tag_id_7 = models.CharField(max_length=100000)  # 精彩书摘
    #上面可能没有
    content = models.CharField(max_length=10000) #大段的文字

    #京东的8是前言/序言
class Tag(models.Model):
    tagName = models.CharField(max_length=100) # 标签名称
class Writer(models.Model):
    writerName = models.CharField(max_length=100) #作者名称
class BookType(models.Model):
    typeName = models.CharField(max_length=100) #分类名称
class BookFile(models.Model):
    kkdFileId = models.IntegerField() #kkd文件id
    fileName = models.CharField(max_length=1000) #文件全名
    fileTypec = models.CharField(max_length=20)#文件格式
    fileSize  = models.CharField(max_length=100) #文件大小
    kkdBook = models.ForeignKey('Kbook')
    isDownload = models.BooleanField(default=False)

