'''
Program: Calorie
Description: sums the calories you have eaten over a given day

Author: Ben Hopper 30139070
Date: 1/05/2026
Version 1.0
'''

#gather date and calorie data
today_date = input('What is todays date? ')
breakfast_cal = float(input('How many calories did you have for breakfast? '))
lunch_cal = float(input('How many calories did you have for lunch? '))
dinner_cal = float(input('How many calories did you have for dinner? '))
snack_cal = float(input('How many calories did you have for a snack? '))

#sum calories and print result with date
sum_cal = breakfast_cal + lunch_cal + dinner_cal + snack_cal
print(f'Calories for {today_date}: {sum_cal}')