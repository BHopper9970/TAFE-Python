'''
Program: N sided dice roller
Description: rolls dice with n sides n number of times

Author: Ben Hopper 30139070
Date: 24/04/2026
Version 1.0
'''


import random
from tkinter import *
from tkinter import ttk

def roll_dice():
    total = 0
    dice_sides = int(sides.get())
    dice_count = int(count.get())
    results = []

    # for dicecount dice rolled do:
    for n in range(dice_count): 
        roll = random.randint(1, dice_sides) # get roll between 1 and dicesides
        total = total + roll # add roll to total
        print(n + 1, 'roll: ', roll) # print current roll
        results.append(roll)
    output.config(text=total)

    itert = 0
    for r in results:
        print(itert)
        globals()[f'var_{itert}'] = ttk.Label(root, text=results[itert])
        exec(f'var_{itert}.grid(row=5 + {itert})')
        itert = itert + 1
    
    

root = Tk()
results = []
ttk.Label(root, text="How many sides?").grid(row=0)
ttk.Label(root, text="How many dice?").grid(row=1)
ttk.Label(root, text="Total:").grid(row=4)

sides = ttk.Entry(root)
count = ttk.Entry(root)

sides.grid(row=0, column=1)
count.grid(row=1, column=1)

ttk.Button(root, text="Roll", command=roll_dice).grid(column=0, row=3)

output = ttk.Label(root)
output.grid(row=4, column=1)

root.mainloop()
