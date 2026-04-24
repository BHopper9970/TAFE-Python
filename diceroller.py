'''
Program: N sided dice roller
Description: rolls dice with n sides n number of times

Author: Ben Hopper 30139070
Date: 24/04/2026
Version 1.0
'''


import random
dice_sides = int(input('How many sides? '))
dice_count = int(input('How many dice? '))
total = 0 # total dice roll so far
for n in range(dice_count): # for dicecount dice rolled do:
    rand = random.randint(1, dice_sides) # get roll between 1 and dicesides
    total = total + rand
    print(n + 1, 'roll: ', rand)
print('Your total is: ', total)
