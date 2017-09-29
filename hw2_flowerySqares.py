# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 12:02:22 2017
Title: Square and circles
@authors: Reyes Ceballos and Sen Varghese
CUS 602
HW2
Objective: Explore turtle, draw circle and squares as defined by user.
"""
# liberaries used
import turtle
import math

#List of variables
t = turtle
sq = 1 #number of squares (default)
sz = 1 #size of squares (default)

def main():
    '''
    The program draws squares proportionaly within a circle. /n
    The square lenght and number of squares are defined by user
    '''
    s = turtle.Screen()
    s.clear()
       
    try:
        sz = int(input('Enter the length for squares in pixels (e.g. 100): '))
        #
        #Enter if statements here
        #
    except:
        print('Please ehter an integer!')
        main()
        
    try:
        sq = int(input('Enter the number of squares to be drawn (e.g. 6): '))
        #
        #Enter if statements here
        #
    except:
        print('Please ehter an integer!')
        main()     
    
    
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
        
    # draw the circle   
    circle()
    
    # number of squares done in j-loop    
    for j in range(sq):
        
        #color the square looping through these colors
        c = ['red','blue','teal', 'yellow', 'purple']      
        t.fillcolor(c[j % 5])
        t.begin_fill()
        
        #the actual square is drawn at varing speeds in  i-loop (i-loop is in the j-loop)
        for i in range (4):
            t.forward(sz)
            t.right(90)
            t.speed(3 + (i*2))
        
        #stop coloring the square
        t.end_fill()
        
        # draw the next square 360/sq angles to the right
        t.right(360/sq)
           
    #keep turtle open     
    s.mainloop()  
 
main()
