import re

# testing if an input is a prime number from a list of first 25 prime numbers

number = input("Enter any value:")
outcome = re.match("[+]?\d+$", number)
prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 
                          47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]    
if outcome is not None:
    if int(number) in prime_list:
        print('Input is Prime')
    else:
        print('Input is not Prime')
else:
    print('Not a Whole Number')
