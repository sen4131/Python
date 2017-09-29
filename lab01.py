
# Laboratory Lab1
# Author: Sen Varghese
# Purpose:  compute the two roots of a quadratic equation.
# Import the math module to access function "math.sqrt()".

import math

def main():
    '''Enter the coefficients A, B and C from the quadratic equation \n\
    (A * x**2 + B * x + C = 0) to get the roots of the equation'''
    
    # coefficient as variables by user
    A = float( input( "\nEnter the coefficient A: " ) )
    B = float( input( "\nEnter the coefficient B: " ) )
    C = float( input( "\nEnter the coefficient C: " ) )
    
    # coefficients
    print( "\nThe coefficients of the equation:\n" )
    print( "  Coefficient A = ", A )
    print( "  Coefficient B = ", B )
    print( "  Coefficient C = ", C )
    
    # **** Replace the following with the calculations of the roots ****
    root1 = ( -B + math.sqrt( B**2 - ( 4*A*C ) ) ) / 2*A  # quadratic formula
    root2 = ( -B - math.sqrt( B**2 - ( 4*A*C ) ) ) / 2*A
    
    # The roots for the quadratic equation displayed for the user 
    print( "\nThe roots of the equation:\n" )
    print( "  Root #1 = ", root1 )
    print( "  Root #2 = ", root2 )

main()



''' 
Answers for lab1:
    
1.  A = 1, B = 0, C = -4
    Root #1 = 2.0
    Root #2 = -2.0
    
2.  A = 1, B = 5, C = -36
    Root #1 = 4.0
    Root #2 = -9.0
    
3.  A = 2, B = 7.5, C = 6
    Root #1 =  -4.627718676730986
    Root #2 =  -10.372281323269014
    
4.  A = 0, B = 3.5, C = 8
    Root #1 = 0.0
    Root #2 = -0.0
    
5.  A = 5, B = 0, C = 6.5
    Root #1 = ValueError: math domain error
    Root #2 = ValueError: math domain error
    
'''