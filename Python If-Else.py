#!/bin/python3

import math
import os
import random
import re
import sys



# This ensures that the code only runs when the file is executed directly,
# and not when imported into another file.
if __name__ == '__main__':
    
    # Take an integer input from the user
    n = int(input().strip())  
    
    # Condition 1: If n is odd (not divisible by 2)
    if n % 2 != 0:
        print("Weird")  
    
    # Condition 2: If n is even and in the range 2 to 5
    elif n % 2 == 0 and n <= 5:
        print("Not Weird")  
    
    # Condition 3: If n is even and in the range 6 to 20
    elif n % 2 == 0 and n <= 20:
        print("Weird")  
    
    # Condition 4: If n is even and greater than 20
    else:
        print("Not Weird")  

          
            
            

