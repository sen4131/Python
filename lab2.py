# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 16:10:19 2017

@author: Sen Varghese
CUS 602: Lab 2

Objective: Python program to display the wind
chill temperature index under certain conditions
"""

# List of variables
# T is the temperature of the air in Fahrenheit
# V is the velocity of the wind, a.k.a. wind speed, in miles per hour (MPH)
# TWC is the wind chill temperature calculated using the formula

# Question 1
a = [10.0,0.0,-10.0] # sample temperatures inserted into list
b = [15,25,35] # sample wind speed inserted into list

for i in range(3):
    TWC = 35.74 + 0.6215 * a[i] - 35.75 * b[i] ** 0.16 + 0.4275 * a[i] * b[i] ** 0.16
    #text = str('for Temperature '+ a[i] + ' and wind speed '+ b[i] + ' the wind chill temp is ')
    print('for Temperature ',a[i],'and wind speed ',b[i], 'the wind chill temp is ', round(TWC,2))
        
        
# Question 2: Function for wind chill temperature
def main():
    'calculates wind chill temp for tepm(T) and wind speed(V)'
    # numbers entered by user
    T = int(input('\nEnter temp: '))
    V = int(input('Enter velocity: '))
    
    # answer is calculated
    TWC = 35.74 + 0.6215 * T - 35.75 * V ** 0.16 + 0.4275 * T * V ** 0.16
    print('The wind chill temp is ' , round(TWC,2))

main()
