#-*-coding:utf-8-*-
from __future__ import division
import random
import math
import matplotlib.pyplot as plt
#由a-b运行获得随机数，c决定是否是整数
# ab大小无所谓，均可实现
# x >= a
# x <= b
# c 为精度,1为整数类型，0为浮点数类型
#*************hm_random********************************************
def hm_random(a,b,c):
    num = random.random()
    cz = b - a
    num = cz*num + a
    if c == 1:
        return random.randint(a, b)
    else:num = num
    return num
#**************hm_plt***********************************************
# 简易的图形化
# x为传入一个数组
# ispause为是否要进行暂停展示图形
# 因为简洁所以不加入更多功能
def hm_plt(x,ispause):
    Fig = plt.figure(figsize=(8,4))
    Ax = Fig.add_subplot(111)
    Ax.plot(x)
    Fig.show()
    if ispause == 1:
        input()
    else:
        nonum = 0
#**********************************************************************
def test_hm_random():
        num_list = []
        num_tj = [0,0,0,0,0,0,0,0,0,0,0]
        for eee in range(1100):
            for x in range(100):
                num_list.append(hm_random(0,10,1))
            num_list.sort()
            for num in num_list:
                if num == 0:
                    num_tj[0] = num_tj[0]+1
                if num == 1:
                    num_tj[1] = num_tj[1]+1
                if num == 2:
                    num_tj[2] = num_tj[2]+1
                if num == 3:
                    num_tj[3] = num_tj[3]+1
                if num == 4:
                    num_tj[4] = num_tj[4]+1
                if num == 5:
                    num_tj[5] = num_tj[5]+1
                if num == 6:
                    num_tj[6] = num_tj[6]+1
                if num == 7:
                    num_tj[7] = num_tj[7]+1
                if num == 8:
                    num_tj[8] = num_tj[8]+1
                if num == 9:
                    num_tj[9] = num_tj[9]+1
                if num == 10:
                    num_tj[10] = num_tj[10]+1
            print num_tj

            if eee == 0:
                num_start = []
                num_start = num_start + num_tj
            if eee == 10:
                num_end = num_tj
                print num_end
                print num_start
                ita = iter(num_end)
                itb = iter(num_start)
                num_bl = []
                for num in range(11):
                   num_bl.append(itb.next()/ita.next())
                X1 = range(0, 11)
                Y1 = num_bl
                Fig = plt.figure(figsize=(8,4)) # Create a `figure' instance
                Ax = Fig.add_subplot(111) # Create a `axes' instance in the figure
                Ax.plot(X1, Y1)# X2, Y2) # Create a Line2D instance in the axes
                Fig.show()
            X1 = range(0, 11)
            Y1 = num_tj
            Fig = plt.figure(figsize=(8,4)) # Create a `figure' instance
            Ax = Fig.add_subplot(111) # Create a `axes' instance in the figure
            Ax.plot(X1, Y1)# X2, Y2) # Create a Line2D instance in the axes
            Fig.show()
        input()


if __name__ == '__main__':
    print 1
