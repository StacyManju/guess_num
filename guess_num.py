# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 07:14:44 2022

@author: jenny
"""

import random

start_num = int(input('請輸入猜數字範圍的起始值: '))
end_num = int(input('請輸入猜數字範圍的末端值: '))

r = random.randint(start_num, end_num)
#print(r)
count = 0

while True:
    count = count +1 
    guess_num = int(input('請猜數字: '))
    if guess_num == r :
        print('您猜對號碼了!')
        print('這是您猜的第', count ,'次')
        break
    elif guess_num < r:
        print('您猜的號碼比正確答案小 請繼續往上猜')
    elif guess_num > r:
        print('您猜的號碼比正確答案大請繼續往下猜')
    else:
        print('只能猜1~100的整數')
    
    print('這是您猜的第', count ,'次')
    