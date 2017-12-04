#-*-coding = utf-8 -*-
import chardet
import urllib.request as req
from lxml import etree
def hm_open(url,coding,filename):
    filename = filename + '.html'
    a = req.build_opener()
    a.addheader = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')]
    c = a.open(url).read()

    read_coding = chardet.detect(c)
    print (read_coding)

    string = str(c,coding,'ignore')
    f = open(filename,'w',encoding = 'utf-8')
    f.write(string)
    f.close()
    return string

def hm_xpath(string,xpath):
    result
    html = etree.HTML(string)
    result = html.xpath(xpath)
    return result

if __name__ == '__main__':
    #hm_open('http://www.baidu.com/','utf-8','test')
    #print (result)
