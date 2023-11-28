"""
2023-11-27

This code solves the euler project's problem

"If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000."

My solution is a simple CLI in which you parse a number and the output are all the multiples of 3 and 5 of the 
parsed number and the sum of the these multiplies.
"""

################################################################################################################################################################
################################################################################################################################################################
def consecutive_integer_generator(x):
    """
    This method take an integer x as input and return all the number between 3 and x-1 in a list.
    
    ******************************************************
    ******************************************************
    INPUT:
    - x : int
        the input number
    ******************************************************
    OUTPUT:
    - integer_generator 
        a list with all the number between 3 and x-1
    """
    #the input number must be an integer
    if not isinstance(x, int):
        raise TypeError("The input must be an integer")
    
    #the input number have to be a positive integer
    if x <= 0:
        raise ValueError(f"{x} is smaller than zero")
    
    #return a list with number from 3 to x-1
    return list(range(3, x))
################################################################################################################################################################
################################################################################################################################################################    

################################################################################################################################################################
################################################################################################################################################################
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
    if not all(isinstance(num, int) for num in listed_number):
        raise ValueError("All the number in the list must be integer number.")

    return [num for num in listed_number if num % 3 == 0 or num % 5 == 0]
################################################################################################################################################################
################################################################################################################################################################


################################################################################################################################################################
################################################################################################################################################################            
def sum_all_parsed_number(integer_list):
   """
   This method sum all the integer number parsed as a list and return the value
    
   ******************************************************
   ******************************************************
   INPUT:
   - integer_list
       the input list
   ******************************************************
   OUTPUT:
   - the sum of the element in the input list
   """             
   if not all(isinstance(num, int) for num in integer_list):
        raise ValueError("All the number in the list must be integer number.")        
   return sum(integer_list)
################################################################################################################################################################
################################################################################################################################################################    



#print(sum_all_parsed_number(multiplies_of_3_and_5(consecutive_integer_generator(16))))   
