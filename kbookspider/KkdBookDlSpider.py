'''
图书下载
未测试
'''
import  requests
import os
from .models import BookFile

cookies = dict(UM_distinctid='15b186506507c8-0fcf6ba7c21c1b-6a11157a-1fa400-15b18650651881', cisession='a031fb39cb885095fcec667358048812a0efe95b',
               CNZZDATA1000201968='357788958-1490760633-https%253A%252F%252Fkankandou.com%252F%7C1492603844',
               Hm_lvt_f805f7762a9a237a0deac37015e9f6d9='1491390312,1491804274,1492176634,1492606366',
               Hm_lpvt_f805f7762a9a237a0deac37015e9f6d9='1492606378')
headers = {"Accept": "text/html,application/xhtml+xml,application/xml;",
            "Accept-Encoding": "gzip",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Referer": "https://kankandou.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
            }
baseBookDir = 'E:/book'
def downloadFile(bookFile):
    fileid = bookFile.kkdFileId
    bookid = bookFile.kkdFileId.kkdBookId
    fileurl = '%s%s%s%s%s' % ('https://kankandou.com/download/file/', bookid, '/', fileid, '.hmlt')
    res2 = requests.get(fileurl, cookies=cookies, headers=headers)
    path = createPath(bookid)
    with open(path+'\\'+bookFile.fileName, 'wb') as code:
        code.write(res2.content)
def createPath(bookid,baseBookDir = r'E:\book'):
    path = '%s%s%s'% (baseBookDir, "\\", bookid)
    os.makedirs(os.path.dirname(r'E:\book\123\aaa.txt'), exist_ok=True)
    return path

#执行程序
while True:
     qs = BookFile.objects.filter(isDownload=False)[:20] # 查询未下载的文件
     if qs.exists():
         for e in qs:
             downloadFile(e)
             e.isDownload = True
             e.save()
     else:
         print('no book not download in db　break')
         break






