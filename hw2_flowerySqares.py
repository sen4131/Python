# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 12:02:22 2017
Title: Square and circles
@author: Nes!

some examples:
#https://michael0x2a.com/blog/turtle-examples
"""

import turtle
import math
import time


#List of variables
t = turtle

print('\nThis program will draw a circle. ')
print('It will then proceed to add squares in the circle ')
        
try:
    sz = eval(input('Enter the length for squares in pixels: '))
except:
    
    while type(sz) != int:
        if type(sz) == str:
            print('Please enter an integer')
            sz = input('Enter the length for squares in pixels: ')
        elif type(sz) == float:
            print('How about you enter an integer instead?')
            sz = input('Enter the length for squares in pixels: ')
        elif sz == 0:
            print('You really want to draw a square with 0 px?')
            sz = input('Enter the length for squares in pixels: ')
        else:
            print('OK, now lets get the number of squares')
        
sq = eval(input('Enter the number of squares to be drawn: '))
#function to draw a circle
def circle():
    'Just a circle with a grey shade'
    hyp = math.sqrt(sz**2 + sz**2)
    t.penup()
    t.setposition(0,-hyp)
    t.pendown()
    t.fillcolor('grey')
    t.begin_fill()
    t.circle(hyp)
    t.end_fill()
    t.penup() 
    t.home()
    t.pendown()

circle()


def main():
    '''
    The program draws squares proportionaly within a circle. /n
    The square length and number of squares are defined by user
    '''
    
    # draw the circle
    
    # number of squares done in j-loop    
    for j in range(sq):
        
        #color the square looping through these colors
        c = ['red','blue','teal', 'yellow', 'purple', 'pink', 'violet', 
             'green', 'orange', 'indigo', 'black', 'white', 'brown', 'cyan',
             'medium sea green', 'DeepPink', 'DeepSkyBlue', 'gold', 'HotPink']      
        turtle.fillcolor(c[j % len(c)])
        turtle.begin_fill()
        
        #the actual square is drawn at varing speeds in  i-loop
        for i in range (4):
            turtle.forward(sz)
            turtle.right(90)
            t.speed(3 + (i*2))
        
        #stop coloring the square
        turtle.end_fill()
        
        # draw the next square 360/x angles to the right
        turtle.right(360/sq)
        
    #keep turtle open     
    
    time.sleep(5)
 
main()
