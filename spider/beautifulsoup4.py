from bs4 import BeautifulSoup
import hm_url
import time
import requests
if __name__ == '__main__':
    # url = 'http://www.xdowns.com/soft/'
    # html = hm_url.hm_open(url,'gb2312','test')
    #
    # #创建一个bs对象，以lxml解析
    # soup = BeautifulSoup(html,'lxml')
    # #输出格式化
    # print (soup.prettify())
    # #find_all(name,attrs,recursive,text,**kwargs)
    # #查找所有
    # #bs.find("input",attr={"name":"_xsrf"}).get("value")
    # print (soup.find_all('a'))
    url = 'https://www.zhihu.com/#signup'
    get = hm_url.hm_req_session(url,'utf-8','test','html','w')
    bs = BeautifulSoup(get,'lxml')
    xsrf = bs.find("input",attrs={"name":"_xsrf"}).get("value")
    print (xsrf)
    pic_url = 'https://www.zhihu.com/captcha.gif?r=%d&type=login&lang=cn'%(time.time() * 1000)
    print (pic_url)

    hm_url.hm_req_session(pic_url,'utf-8','test','jpg','wb')
    text = input()
    data = {
    "_xsrf" : xsrf,
    "email" : "693760891@qq.com",
    "password" : "Zc2582069",
    "captcha" : text
    }
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}

    sess = requests.session()
    get = sess.post("https://www.zhihu.com/login/email",data = data,headers = header)
    print (get.content)
