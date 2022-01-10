import re

# testing if an input is a perfect square from a list of first 25 prime numbers

number = input("Enter any value:")
outcome = re.match("[+]?\d+$", number)
perfectsq_list = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 
                  144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 
                  484, 529, 576, 625]    
if outcome is not None:
    if int(number) in perfectsq_list:
        print('Input is a Perfect Square')
    else:
        print('Input is not a Perfect Square')
else:
    print('Not a Whole Number')