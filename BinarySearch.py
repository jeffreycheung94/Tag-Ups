# -*- coding: utf-8 -*-
"""
Created on Sat May  2 16:44:03 2020

@author: jeffr
"""


#BinarySearchAlgo

#create a random list of numbers from 0 to 100 with a difference of two between each number


 
def binarySearch(array, numberGuess):    
    first = 0 
    last = len(array) - 1 
    found = False
    while (first <= last and not found):
        arrayMiddle = round((first + last) / 2 )
        if numberGuess == randomNumbers[arrayMiddle]:
                print('your number is at entry number ', arrayMiddle)
                found = True
                break
        else:
            if numberGuess < randomNumbers[arrayMiddle]:
                last = arrayMiddle - 1 
            elif numberGuess > randomNumbers[arrayMiddle]:
                first = arrayMiddle + 1
    print('your number isnt in the array')
def main():
    randomNumbers = []
    
    i = 0
    while i < 102: 
        randomNumbers.append(i)
        i = i + 2
    
    while True:
        try:
            numberGuess = int(input('Please input a bungholio number to see if it is in the list'))
        except ValueError:
            print('Please enter an integer value')
        else:
            break
        
    binarySearch(randomNumbers, numberGuess)