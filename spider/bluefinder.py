import urllib.request as request
from lxml import etree
import chardet
import hm_url
if __name__ == '__main__':
    content = hm_url.hm_open('http://www.xdowns.com/soft/','gb2312','test')
    e = hm_url.hm_xpath(content,"//a[@class='item_link']/@href")
    for i in e:
        print (i)
