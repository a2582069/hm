#-*- coding:utf-8 -*-

import random
import hmmath

def _easy_wei(gn,a,b,c,d,e,isprint = None):
    if isprint == 1:
        print 'gn = ' + str(gn)
        print 'a = ' + str(a)
        print 'b = ' + str(b)
        print 'c = ' + str(c)
        print 'd = ' + str(d)
        print 'e = ' + str(e)

    if gn == 1:
        a[c[0]] = 1
        a[c[1]] = 1
        return a
    if gn == 2:
        i = 1
    if gn == 3:
        i = 1

    return 0

if __name__ == '__main__':
    weight = []
    price= []
    for e in range(5):
        weight.append(hmmath.hm_random(10,100,1))
        price.append(hmmath.hm_random(10,100,1))
    print 'weight' + str(weight)
    print 'price' + str(price)
    print u"初始基因组"
    gene_a = [0,0,0,0,0]
    gene_b = [0,0,0,0,0]
    sj1 = [hmmath.hm_random(0,4,1),hmmath.hm_random(0,4,1)]
    sj2 = [hmmath.hm_random(0,4,1),hmmath.hm_random(0,4,1)]
    sj3 = [hmmath.hm_random(0,4,1),hmmath.hm_random(0,4,1)]
    sj4 = [hmmath.hm_random(0,4,1),hmmath.hm_random(0,4,1)]
    gene_a = _easy_wei(1,gene_a,sj2,sj1,0,0)
    gene_b = _easy_wei(1,gene_b,sj3,sj4,0,0)
    print gene_a
    print gene_b
