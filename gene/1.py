import random
import hmmath
if __name__ == '__main__':
    weight = []
    price= []
    for e in range(5):
        weight.append(hmmath.hm_random(10,100,1))
        price.append(hmmath.hm_random(10,100,1))
    print weight
    print price

    start = [1,1,1,1,1]
