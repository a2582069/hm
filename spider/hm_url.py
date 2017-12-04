#-*-coding = utf-8 -*-
import chardet
import urllib.request as req
#from lxml import etree
import requests
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

def hm_req_session(url,coding,filename,ftype,open_file_by):
    filename = filename + '.'+ ftype
    user_agent = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64)"}
    a = requests.session()
    c = a.get(url,headers = user_agent)
    c.encoding = coding
    ct = c.text
    #print (c.encoding)
    if open_file_by == 'wb':
        f = open(filename,open_file_by)
        f.write(c.content)
        f.close()
    else:
        f = open(filename,open_file_by,encoding = 'utf-8')
        f.write(ct)
        f.close()
    return ct

def hm_xpath(string,xpathx):
    html = etree.HTML(string)
    result = html.xpath(xpathx)
    return result

if __name__ == '__main__':
    url = 'https://www.zhihu.com/#signin'
    url1 = 'http://www.baidu.com/'
    #content = hm_req_session(url,'gb2312','test','html','w')
    #urltest = 'http://www.xdowns.com/soft/'
    content = hm_open(url,'gb2312','zhihu')
    print (content)
    e = hm_xpath(content,"//a[@class='item_link']/@href")
    for i in e:
        print (i)
    print
