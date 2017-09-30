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
sz = '' # length of the sides of the square
sq = '' # number of squares to be drawn


def about():
    print('\nThis program will draw a circle. ')
    print('It will then proceed to add squares in the circle ')
    print('You\'ll need to enter the size and number os squares when asked')

def size ():
    'To ensure user enter a valid number for pixel length between 25 and 200'
    global sz
    while type(sz) != int or sz < 25 or sz > 200:
        try:
            sz = int(input('\nEnter the length for squares in pixels (between 25 and 200): '))
            
            if sz < 25:
                print('\nThat is too small')
                size()
            elif sz > 200:
                print('\nThat is too big')
                size()
            else:
                print('\nOK! We\'re nearly there!')
        
        except:
            print('\nPlease enter an integer!')
      
def squares():
    'To ensure user enter a valid number of square between 1 and 30'
    global sq
    while type(sq) != int or (sq == 0) or (sq > 30):
        try:
            sq = int(input('\nEnter the number of squares to be drawn (between 1 and 30): '))
            
            if sq == 0:
                print('\nThat is too small')
                squares()
            elif sq > 30:
                print('\nThat is too big')
                squares()
            else:
                print('\nOK! We\'re good to go!')
                print('\nTake a look at the turtle canvas...')
                
        except:
            print('\nPlease enter an integer!')
        
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

def drawSquare():
    #the actual square is drawn at varing speeds in  i-loop
    for i in range (4):
        turtle.forward(sz)
        turtle.right(90)
        t.speed(3 + (i*2))
        
def main():
    '''
    The program draws squares proportionaly within a circle. /n
    The square length and number of squares are defined by user
    '''
    about()
    # correct variables
    size()
    squares()
    # draw the circle
    circle()

    # number of squares done in j-loop    
    for j in range(sq):
        
        #color the square looping through these colors
        c = ['red','blue','teal', 'yellow', 'purple', 'pink', 'violet', 
             'green', 'orange', 'indigo', 'black', 'white', 'brown', 'cyan',
             'medium sea green', 'DeepPink', 'DeepSkyBlue', 'gold', 'HotPink']      
        
        turtle.fillcolor(c[j % len(c)])
        turtle.begin_fill()
        #function draws squares
        drawSquare()
        #stop coloring the square
        turtle.end_fill()
        # draw the next square 360/x angles to the right
        turtle.right(360/sq)
        
    #keep turtle open     
    time.sleep(5)

main()
