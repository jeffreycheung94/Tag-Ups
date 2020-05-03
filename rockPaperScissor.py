# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 22:21:34 2020

@author: jeffr
"""

#rockPaperScissors 

import random
movesAvailable = ['rock', 'paper', 'scissor']
computersMove = movesAvailable[random.randint(0,2)]
#print(computersMove)
print('Please make a move (rock, paper or scissor)')
playerMove = input()
#can combine lines 14 and 15, add text inside input statement
while True: 
    #check to see if we have a tie
    if str(playerMove) == computersMove:
        print('We have tie!')
    #playersMove is a scissor
    elif str(playerMove) == 'scissor': 
        if str(computersMove) == 'rock':
            print('LOSER')
        elif str(computersMove) == 'paper': 
            print('WINNER WINNER CHICKEN DINNER')
    #playersMove is paper
    elif str(playerMove) == 'paper': 
        if str(computersMove) == 'rock':
            print('WINNER WINNER CHICKEN DINNER')
        elif str(computersMove) == 'scissor': 
            print('LOSER')
    #playersMove is a rock
    elif str(playerMove) == 'rock': 
        if str(computersMove) == 'scissor':
            print('WINNER WINNER CHICKEN DINNER')
        elif str(computersMove) == 'paper': 
            print('LOSER')
    break
        


