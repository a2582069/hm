import json
import jsonpath
import hm_url

if __name__ == '__main__':
    url = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json'
    e = hm_url.hm_open(url,'utf-8','test')
    uncodestr = json.loads(e)
    city = (jsonpath.jsonpath(uncodestr,'$..name'))
    print (jsonpath.jsonpath(uncodestr,'$..name'))

    a =json.dumps(city,ensure_ascii=False)
    print (a)
