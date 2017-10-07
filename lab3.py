# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 15:48:10 2017

@author: Sen
"""
def main():
    ''' 
    Python program which inputs a series of integers and processes them. 
    Even & odd numbers are added and counted.
    '''
    
    # list of variables
    lst = []
    x = ''
    evenList = []
    oddList = []
    countEven = 0
    countOdd = 0
    
    #user inputs the values as integer
    while x != 0:
        try:
            x = int(input('\nEnter a number (0 terminates): '))
        except:
            print('\nplease enter an integer')
        if x > 0:
            lst.append(x)
        elif x < 0:
            print('\nYou\'ve entered a negative number')
    
    # loop through the full user list and splits and count the numbers
    # based on whether even or odd number           
    for i in lst:
        if i%2 == 0:
            countEven += 1
            evenList.append(i)
        elif i%2 == 1:
            countOdd += 1
            oddList.append(i)
    
    #sum of all even number
    sumEven = sum(evenList)
    #sum of all odd number
    sumOdd = sum(oddList)
    
    
    #all the output printed for user
    print('\nyou\'ve entered '+ str(countEven) + ' even numbers')
    print('\nsum of even numbers: '+ str(sumEven))
    print('\nyou\'ve entered '+ str(countOdd) + ' odd numbers') 
    print('\nsum of odd numbers: '+ str(sumOdd))    
    print('\nTotal of ' + str(len(lst)) + ' positive numbers')

#    print(lst)

main()
