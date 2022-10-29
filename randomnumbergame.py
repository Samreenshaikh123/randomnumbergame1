# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 19:37:07 2022

@author: user
"""

import random
computer=random.randint(1,100)
player=0
tries=0
print('guess my number game')
while (player!=computer):
    player=int(input('enter your guess:'))
    tries=tries+1
    if player<computer :
        print ('Too low,try again')
    elif player>computer :
        print('Too high,try again')
    else:
        print('Correct!,you got in ',tries,'tries')
        