'''
抓取分页信息中的
书名 豆瓣url
作者
分类信息


'''

from bs4 import BeautifulSoup
import  requests
#from .models import Kbook,Tag,Writer
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
        pass
   else:
       print('an error found ')





if __name__== '__main__':
    spiderPageInfo(getPageUrl(4))
