import threading
from queue import Queue
from lxml import etree
import requests
import hm_url
import json

class ThreadCrawl(threading.Thread):
    def __init__(self,threadName,page_queue,data_queue):
        #threading.Thread.__init__(self)
        #调用父类初始化方法
        super(ThreadCrawl,self).__init__()
if __name__ == '__main__':
    page_queue = Queue(10)

    for i in range(1,11):
        page_queue.put(i)
    data_queue = Queue()

    Threadcrawl = []
    crawlList = ["采集线程1号","采集线程2号","采集线程3号"]
    for threadName in crawlList:
        thread = ThreadCrawl(threadName,page_queue,data_queue)
        thread.start()
        Threadcrawl.append(thread)
