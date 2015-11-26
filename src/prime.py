# -*- encoding: utf-8 -*-
'''
Created on 2014年7月12日

@author: xun.ms
'''

# one line
def prime_list(n=100):
    return [i for i in range(2, n) if not [j for j in range(2, int(i / 2) + 1) if i % j == 0]]

# generator
def prime_generator(n=100):
    for i in range(2, n):
        if not [j for j in range(2, int(i / 2) + 1) if i % j == 0]:
            yield i

# 传统方法
def prime_old(n=100):
    for i in range(2, n):
        flag = True
        for j in range(2, int(i / 2) + 1):
            if(i % j == 0):
                flag = False
                break
        if flag:
            yield i

if __name__ == '__main__':
    print(prime_list())
    print([i for i in prime_generator()])
    print([i for i in prime_old()])