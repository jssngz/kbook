import django
django.setup()
from lxml import html,etree
import re
import requests
import sqlite3
from kbookspider.models import Kbook,Tag,Writer,BookType
#import kbookspider.models as models
'''
抓取分页信息中的
书名 豆瓣url
作者
分类信息
'''
#拼接分页信息
def getPageUrl(page):
    if(page==1):
        return "https://kankandou.com/"
    else:
        return "https://kankandou.com/book/page/"+str(page)

#抓取分页页面上的信息
def spiderPageInfo(pageUrl):
   header = {
       'Connection': 'Keep-Alive',
       'Accept': 'text/html, application/xhtml+xml, */*',
       'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
       'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'
   }
   cookie = {
       'UM_distinctid': '15b5304235b273-08009154354043-64191279-100200-15b5304235d15c',
       'cisession': '2c04b6b2d9751e1c0ed6599a1213a645e8b2df6a',
       'CNZZDATA1000201968': '801740819-1491745617-%7C1492936303',
       'Hm_lvt_f805f7762a9a237a0deac37015e9f6d9': '1491746432,1492908064',
       'Hm_lpvt_f805f7762a9a237a0deac37015e9f6d9': '1492938846'
   }
   respon = requests.get(pageUrl, cookies=cookie, headers=header, timeout=5000)
   print(respon.status_code)
   if(respon.status_code==200):

        praseHtmlToDB(respon)
        print(respon.text)
        pass
   else:
       print('an error found ')

def praseHtmlToDB(html_str):
    baseXpath = "/html/body/div[1]/div[1]/ul[1]/li["
    doc2 = etree.HTML(html_str)
    for i in range(1,17):
        xpath_bookurl = baseXpath + str(i) + "]/div[2]/h3/a"
        xpath_img = baseXpath + str(i) + "]/div[1]/a/img"
        xpath_writer = baseXpath + str(i) + "]/div[2]/p[1]/a"
        xpath_type = baseXpath + str(i) + "]/div[2]/p[2]/a"
        book_id = getIdFromBookDetailUrl(doc2.xpath(xpath_bookurl)[0].get("href"))
        book_name = doc2.xpath(xpath_bookurl)[0].text
        writer_name = doc2.xpath(xpath_writer)[0].text
        type_name = doc2.xpath(xpath_type)[0].text
        img_src = doc2.xpath(xpath_img)[0].get("src")
        storeInfoToDB(book_id,book_name,img_src,writer_name,type_name)
 #   from .models import Kbook, Tag, Writer
 def
#保存数据在db中
def storeInfoToDB(book_id,book_name,img_src,writer_name,type_name):
    conn  = sqlite3.connect("../db.sqlite3")


    writerObj = Writer.objects.get_or_create(writerName=writer_name)
    writerObj.save()
    bookTypeObj = BookType.objects.get_or_create(typeName=type_name)
    bookTypeObj.save()
    kbookObj = Kbook.objects.get_or_create(kkdBookId=book_id)
    kbookObj.kkdBookId = book_id
    kbookObj.bookName = book_name
    kbookObj.doubanImgSrc = img_src
    kbookObj.writer = writerObj
    kbookObj.bookType = bookTypeObj
    kbookObj.save()
def getIdFromBookDetailUrl(url):
    regex = re.compile(r'view/\d+', re.I)
    m = regex.search(url)
    if m:
        value = m.group(0)
        return value.split("/")[1]
    else:
        return None



if __name__== '__main__':
    #spiderPageInfo(getPageUrl(4))
    storeInfoToDB(123,"zhangsandeshu","http://baidu.com","朱帅","文学")
