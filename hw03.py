# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 17:43:55 2017

@author: Nesquick & The Don Reyes
CUS 620
HW3

@Title: Master Mind

@Description: A master mind game  using letters instead of colors: RYBGWO
    (representing Red, Yellow, Blue, Green, White, Orange).
    The player gets eight guesses; 
    if they do not guess the key in 8 guesses, they lose.

@Program is split in 4 steps:
    1 generate 4 random colors
    2 generate 4 colors from user max of 8 times
    3 compare user colors to computer colors each time to max 8 times
    4 prints history after the 8 tries
    
@sidenotes: this HW was done while listening to some serious dubstep!!
"""
def main():
    
    tries = 3   #No of tries user gets
    col = ['R','Y','B','G','W','O']   #valid colors
    
    '_hist variables are used to log the player history'
    exact_hist = [] 
    correct_hist = []
    
#1 generate 4 random colors

    import random
    comp = []
    counter1 = 0
    
    while len(comp) < 4:
        
        a = random.randint(0,5)
        b = col[a]
        
        if b not in comp:
            comp.append(b)
            counter1 += 1
        else:
            continue
            
#    print(comp)
   
#2 generate 4 colors from user max of 8 times

    for loop in range(tries):
        
        user = [] #saves the valid user entry into list
        u_counter = 0
        
        while u_counter < 4:
            
            x = input('\nEnter a color code: ')
            u_colors = x.upper()
            
            if len(u_colors) == 4:
            #if statement only runs if user inputs exactly 4 characters    
                for color in u_colors:
                    if color not in user and color in col:
                        user.append(color)
                        u_counter += 1
                    else:
                        print('\nTry again!')
                        break
            else:
                print('\nEnter 4 valid letters!\n')
                
#    print(user)
               
#3 compare user colors to computer colors

        exact = 0 #var for counting the exact matches
        correct = 0 #var for counting the correct matches that arent exact
        
        for i, ch in enumerate(user):
            if ch == comp[i]:
                exact += 1
            elif ch in comp:
                correct += 1
                
        exact_hist.append(exact)
        correct_hist.append(correct)
        
        if exact == 4:
            print('\nYou Win!!!')
            print('\nIt took ', loop + 1 ,' guesses')
            print('\nYour record:')
            print('\nExact hits ', exact_hist)
            print('\nCorrect    ', correct_hist)
            break
        else:        
            print('\nCorrect color and position count: ',exact)
            print('\nCorrect color, but wrong position count: ',correct)
            
# 4 prints after the 8 tries

    print('\nYour record:')
    print('\nExact hits ', exact_hist)
    print('\nCorrect    ', correct_hist)       

main() 