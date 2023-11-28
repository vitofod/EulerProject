import argparse 
from enum import Enum
import multiples_of_3_and_5

"""
The main.py manages the user interface through a Command Line Interface (CLI)
"""

################################################################################################################################################################
################################################################################################################################################################
class Handler(Enum):
    '''
    This simple enum class handles the options callable by the CLI
    
    ......................................
    Attributes
    ......................................
    sum_multiplies: is selected, you can recall the euler projectt's #1
    
    '''
    sum_multiplies = 'sum_multiplies'
    #spectrum = 'spectrum'
    #all = 'all'

    def __str__(self):
        return self.value
    
###############################################################################################################################################################
###############################################################################################################################################################

def main(): 
    '''
   This is the main methods. From here i manage input data from CLI. 
    '''
    parser = argparse.ArgumentParser(description="CLI for solving Euler Project Problems")
    
    #I describe the first, the others are created with the same logic
    #data input path
    parser.add_argument(
        "-p1",
        "--problem-1",
        action='store_true',  
        help="Solves Euler Project's Problem #1. Need the option -n followed by a positive integer"
    )
    
    #input p1 options
    parser.add_argument(
        "-n", 
        "--number", 
        type=int, 
        required=False,                            
        help="The number to parse to Euler project's number 1."
        )
    
    args = parser.parse_args()
    
    #I manage the inputs -p1
    if args.problem_1:
        if args.number is None:
            parser.error("--number is required with --problem-1")
        else:
            # Chiama le funzioni dal modulo e stampa i risultati
            all_numbers = multiples_of_3_and_5.consecutive_integer_generator(args.number)
            multiplies = multiples_of_3_and_5.multiplies_of_3_and_5(all_numbers)
            sum_of_multiplies = multiples_of_3_and_5.sum_all_parsed_number(multiplies)
            print(f"Sum of all multiples of 3 and 5 below {args.number} is: {sum_of_multiplies}")
            
################################################################################################################################################
################################################################################################################################################            

if __name__ == "__main__":
    main()