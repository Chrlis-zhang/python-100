#coding:utf-8
'''
有四个数字：1、2、3、4 能组成多少个互补相同且无重复数字的三位数

'''
for i in range(1,5):
    for s in range(1,5):
        for d in range(1,5):
            if (i != s ) and (i != d) and (d != s): #判断3个数字是否相同
                print(i,s,d)
