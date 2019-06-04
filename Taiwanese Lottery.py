# coding=UTF-8
__author__="Matt Wang"
'''
大樂透模擬器ver2.00
輸入數量看要買多少張電腦選號
製作日期：14/05/2019 - 21/05/2019
'''
import random

print(" ")
while True:
    try:
        count=int(input("請輸入你要買幾張大樂透電腦選號: "))
        num=int(count)
        break
    except:
        print("請輸入整數數字喔！")

print(" ")

term=108000047
win=[2,7,12,21,23,45]
winS=10
print("大樂透第 %d 期"%term)
print("本期號碼： %s, 特別號: %s"%(win,winS))


# hit of normal number

total=0 #for total price you win

for c in range(1,count+1):
    print(" ") #space
    own=random.sample(range(1,49),6) 
    print("你的第 %d 張大樂透電腦選號: %s"%(c,own))


    hit=0
    for i in range(6):
        for j in range(6):
            if (own[i]==win[j]):
                hit+=1 #hit of normal number

    if (hit!=0):
        print("恭喜您！您中了 %d 個號碼"%hit)
    else:
        print("喔喔！您沒有中的號碼！")


    cs=0
    for i in range(6):

        if (own[i]==winS):
            print("恭喜您！您中了本期的特別號！")
            cs+=1 #hit of special number


    # how much do you win (hit & cs)


    if (hit==6):
        print("恭喜您！您中了本期的頭獎！獎金是: 301,272,731 元新台幣！")
        total+=301272731
    elif (hit==5 and cs==1):
        print("恭喜您！您中了本期的貳獎！獎金是: 798,313 元新台幣！")
        total+=798313
    elif (hit==5):
        print("恭喜您！您中了本期的參獎！獎金是: 39,987 元新台幣！")
        total+=39987
    elif (hit==4 and cs==1):
        print("恭喜您！您中了本期的肆獎！獎金是: 8,248 元新台幣！")
        total+=8248
    elif (hit==4):
        print("恭喜您！您中了本期的伍獎！獎金是: 2,000 元新台幣！")
        total+=2000
    elif (hit==3 and cs==1):
        print("恭喜您！您中了本期的陸獎！獎金是: 1,000 元新台幣！")
        total+=1000
    elif (hit==2 and cs==1):
        print("恭喜您！您中了本期的柒獎！獎金是: 400 元新台幣！")
        total+=400
    elif (hit==3):
        print("恭喜您！您中了本期的普獎！獎金是: 400 元新台幣！")
        total+=400
    else:
        print("這張彩卷沒有中獎喔！請再接再厲！")

print(" ") #space
print("-----------結算------------")
print(" ") #space


print("本次您總共買了 %d 張彩卷"%count)
p=count*50
print("一共花費了 %d 元新台幣"%p)
print("總共贏得了 %d 元新台幣"%total)

print(" ") #space
