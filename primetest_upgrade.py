import re

# testing if an input is a prime number using recursion 
# => will work for more numbers until recursive depth is too large

number = input("Enter any value:")
outcome = re.match("[+]?\d+$", number)


def has_a_factor(n,d):
    '''
    returns True if and only if n has a factor between 2 and d inclusive and
    False otherwise
    
    has_a_factor: Nat Nat -> Bool
    requires: n >= 2
    
    Examples:
    has_a_factor(701,700) => False
    has_a_factor(4,3) => True
    '''
    if d <= 1:
        return False
    elif n % d == 0:
        return True
    else: 
        return has_a_factor(n,d-1)

def is_prime(n):
    '''
    returns True if and only if the natural number n is a prime number which 
    means it does not have a divisor other than 1 and itself unless n is 1
    
    is_prime: Nat -> Bool
    
    Examples:
    is_prime(701) => True
    is_prime(4) => False
    '''
    return n >=2 and not(has_a_factor(n,n-1))

if outcome is not None:
    if is_prime(int(number)) == True:
        print('Input is Prime')
    else:
        print('Input is not Prime')
else:
    print('Not a Whole Number')