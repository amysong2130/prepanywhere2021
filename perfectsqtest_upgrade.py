import re
import math

# testing if an input is a perfect square 

number = input("Enter any value:")
outcome = re.match("[+]?\d+$", number)

if outcome is not None:
    sqrt = math.sqrt(int(number))
    result = re.match("[+]?\d+\.?0?$", str(sqrt))    
    if result is not None:
        print('Input is a Perfect Square')
    else:
        print('Input is not a Perfect Square')
else:
    print('Not a Whole Number')