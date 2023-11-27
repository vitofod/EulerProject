"""
2023-11-27

This code solves the euler project's problem

"If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000."

My solution is a simple CLI in which you parse a number and the output are all the multiples of 3 and 5 of the 
parsed number and the sum of the these multiplies.
"""

def decomposition_of_a_number(x):
    """
    This method take an integer x as input and return all the number between 3 and x-1 in a list.
    
    ******************************************************
    ******************************************************
    INPUT:
    - x : int
        the input number
    ******************************************************
    OUTPUT:
    - submultiples 
        a list with all the number between 3 and x-1
    """
    #the input number must be an integer
    if not isinstance(x, int):
        raise TypeError("The input must be an integer")
    
    #the input number have to be a positive integer
    if x <= 0:
        raise ValueError(f"{x} is smaller than zero")
    
    #a list with number from 3 to x-1
    decomposition = []
    for index in range(3, x):
        decomposition.append(index)
    
    return decomposition
    

def multiplies_of_3_and_5(listed_number):
    """
    This method take a list fullfil with integer between 3 and a value x>3 as input and return a list
    with all the number inside the input list that are multiples of 3 and 5.
    
    ******************************************************
    ******************************************************
    INPUT:
    - listed_number 
        the input list fulfill with number between 3 and x>3
    ******************************************************
    OUTPUT:
    - multiples_3_and_5 
        a list with all the submultiples of 3 and 5 inside the input list
    """
    multiplies_of_3_and_5 = []
    
    for element in listed_number:
        #if the element of the list is a multiple of 3 or 5, add the number to the list
        if ((element % 3) == 0 or (element % 5) == 0):
            multiplies_of_3_and_5.append(element)
        
    return multiplies_of_3_and_5    
            
            
            
    
#returned_list = decomposition_of_a_number(16)        
#another_returned_list = multiplies_of_3_and_5(returned_list)    
