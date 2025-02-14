import random as rd
from math import sqrt
from itertools import count, islice
def simpleNum(n):
    num = []
    sim = simple()
    flag = True
    while flag:
        flag = False
        num = []
        for i in range(n):
            num.append(rd.randint(0, 1))
        num[0] = 1
        num[-1] = 1
        number = 0
        for i in range(len(num)):
            number += num[i] * 2 ** (len(num) - 1 - i)
#        print(number)
        for i in sim:
            if number % i == 0 and number != i:
                flag = True
#                print('NO in simple')
                break
        if flag:
            continue
        for i in range(5):
            if test(number) == -1:
                flag = True
#                print('NO in test')
                break
    return number


def test(p):
    temp = p - 1
    b = 0
    while temp % 2 == 0:
        temp /= 2
        b += 1
    m = (p - 1) / (2 ** b)
    a = rd.randint(0, p - 1)
    j = 0
#    print(": ", a, " : ", m)
    z = pow(int(a), int(m), int(p))
    if z == 1 or z == p - 1:
        return 1
    while (True):
        if j > 0 and z == 1:
            return -1
        j += 1
        if j < b and z < p - 1:
            z = pow(z, 2, p)
            continue
        elif z == p - 1:
            return 1
        if j == b and z != p - 1:
            return -1


def simple():
    n = 2000
    lst = [2]
    for i in range(3, n + 1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True


def safe_prime():
    N = simpleNum(40)
    while not is_prime((N-1)/2):
        N = simpleNum(40)
    return N