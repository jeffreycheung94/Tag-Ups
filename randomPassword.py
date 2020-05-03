# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 11:11:08 2020

@author: jeffr
"""
def randomPassword(passLength):
    import random as rand
    import string 
    
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    passwordHolder = []
    passwordValueOptions = ['upper', 'lower', 'number']
    
    randomLower = rand.choice(lower_case)
    randomUpper = rand.choice(upper_case)
    

    
    #need to randomly decice between number, upper or lower
    
    for i in range(passLength):
        nextValueDecision = rand.choice(passwordValueOptions)
        if nextValueDecision == 'upper':
           nextValue = rand.choice(upper_case)
           passwordHolder.append(nextValue)
        elif nextValueDecision == 'lower':
           nextValue = rand.choice(lower_case)
           passwordHolder.append(nextValue)
        elif nextValueDecision == 'number':
           nextValue = rand.randint(0,9)
           passwordHolder.append(nextValue)
         
    print(''.join(str(passwordHolder)))
def main():
    while True:
            try:
                passwordL = int(input('How long do you want your password to be? (must be longer than 6 characters) \n'))
                if passwordL> 6:
                    break
                else:
                   raise TypeError 
            except ValueError:
                print('Please enter an integer value')
            except TypeError:
                print('please choose a value greater than 6')
            else:
                break    
    randomPassword(passwordL)
        
main() 