# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 22:12:55 2020

@author: jeffr
"""


#Guessthenumber

import random
playerGuess = 21
randomNumber = random.randint(0,20)
print(randomNumber)
while playerGuess != randomNumber:
    print('Please guess an integer value between 0 and 20')
    playerGuess = (input())
    if playerGuess == randomNumber:
        print('congrats!!! you guessed the right number!!')
    else: 
        continue 