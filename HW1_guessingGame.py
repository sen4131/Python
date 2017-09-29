# -*- coding: utf-8 -*-
"""
Spyder Editor
Author: Reyes Ceballos and Sen Varghese
CUS 602
HW1
Objective: a guessing game that continues until responded gives the correct answer
"""


# defining the answer of the puzzle
import random
H = random.randint(1,9) #Hundreds unit of the answer
U = random.randint(1,9) #Units unit of the answer
T = random.randint(max(H,U),9) #Tens unit of the answer
answer = H*100 + T*10 + U #This the unique generated answer 

#difference between Hundreds and Tens, and Tens and Units of the answer
diff_ht = T - H
diff_ut = T - U

#Question 5 does the puzzle you generate have multiple answers?: 
    #No multiple answers per session


#start game with puzzle stored in variable p
p =  '\n\
Enter a three-digit number whose tens digit \n\
is at least as big as its units digit and \n\
the tens digit is also at least as big as its hundreds digit.\n\
'

#second statement to assist respondend
p2 = '\n\
the Tens digit is ' + str(diff_ut) +' greater than Units digit \n\
and Hundreds digit is ' + str(diff_ht) + ' less than Tens digit.\n\
'


#The main function
def main():
    'a guessing game that continues untill responded gives the correct answer'
    print(p)
    
    #this variable stores the respondends guess
	# Question1. What happens when the user enters a letter instead of a number at the prompt?
    try:
        num_str1 = int(input('Please enter an integer: '))
    except:
        print('Dude! please enter a number!')
        main()
    
    # loop until the right answer is given
    while num_str1 != answer:
        #adjustment for responded not entering a 3digit number (Question 3 & 4)
        if num_str1 < 100 or num_str1 > 999:
            print ('Please enter a 3 digit number\n\
                   ')
            print(p2)
            num_str1 = int(input('Please enter an integer: '))
        
        elif num_str1 > answer:
            print('try again, answer is lower')  
            print(p2)
            num_str1 = int(input('Please enter an integer: '))
            
        elif num_str1 < answer:
            print('try again, the answer is higher')
            print(p2)
            num_str1 = int(input('Please enter an integer: '))
            
    print('You WIN!!')       

main()