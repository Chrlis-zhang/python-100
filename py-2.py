#coding:utf-8
'''
企业发放奖金根据利润提成
利润小于10W时，奖金按照10%
利润大于10W小于20W时，小于10W的部分按照10%，高于10W的按照7.5%
利润大于20W小于40W时，高于20W的部分按照5%
利润大于40W小于60W时，高于40W的部分按照3%
利润大于60W小于100W时，高于60W的部分按照1.5%
利润大于100W时，高于100W的部分按照1%
奖金为成长整型
'''

i = int(input('利润:'))

arr = [1000000,600000,400000,200000,100000,0]   #设置奖金分类
rat = [0.01,0.015,0.003,0.005,0.075,0.1]    #设置奖金提成

r = 0

for idx in range(0,6):
    #print(arr[idx],rat[idx])
    if i > arr[idx]:
        r += (i - arr[idx]) * rat[idx]      #利润计算写入r
        print((i - arr[idx]) * rat[idx])    #利润计算
        i = arr[idx]
print(r)
