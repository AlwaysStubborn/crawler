#-*- coding:utf-8 -*-
#from urllib import request
import requests
#with request.urlopen('https://www.baidu.com') as f:
#    data = f.read()
#    print('Status:', f.status, f.reason)
#    for k, v in f.getheaders():
#        print('%s: %s' % (k, v))
#    print('Data:', data.decode('utf-8'))
import os	
from lxml import html	

#保存知乎的妹子图，先准备一下思路
#1.抓取整个页面，直接用read可不可以呢？好像也是可以的吧，get或者post返回的也是源码吧，试一下
#2.过滤出来图片，名字最好重命名一下
#3.保存
#4.只是抓出来没什么用处啊，能不能分个类？

#准备网页头
Header={'Host':'www.zhihu.com','Connetion':'keep-alive','User-agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/525.13',}

#默认的文件夹名称
DefaultFolderName = 'pic'

#抓取页面，过滤图片
def crawlerPic(url):
    resp = requests.get(url,headers=Header)
    page = resp.content    
    root = html.fromstring(page)    
    imageUrls = root.xpath('//img/@data-actualsrc')
    print('count:',len(imageUrls))
    idx = 0
    for imageUrl in imageUrls:
        print(imageUrl)
        resp = requests.get(imageUrl)
        page = resp.content
        saveImage(page,str(idx)+'.jpg')
        idx+=1
	
#循环保存的方法
def saveImage(content,fileName):
    if (os.path.exists(DefaultFolderName) != True):
        os.mkdir(DefaultFolderName)
    path = os.path.join(DefaultFolderName,fileName)
    with open(path,'wb') as f:
        f.write(content)

#调用
#beauty
DefaultFolderName = 'beautyPic'
#crawlerPic('https://www.zhihu.com/question/49364343')

DefaultFolderName = 'beautyEye'
crawlerPic('https://www.zhihu.com/question/65727199')


#busty
DefaultFolderName = 'bustyPic'
crawlerPic('https://www.zhihu.com/question/58778900')

#print(os.environ.get('PATH'))