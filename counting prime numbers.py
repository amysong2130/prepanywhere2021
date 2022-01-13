import check

# helper function

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

def count_prime(latex):
        '''
        Parameters
        ----------
        latex: list of str
           each element should be a natural number in format of string
        
        Returns
        -------
           returns pandas Series with count of prime numbers
           
        Examples
        --------
        count_prime(['1','4','10','17','71','97']) => 3
        count_prime([]) => 0
        count_prime(['2','4','6','8']) => 0
        count_prime(['1']) => 0
        count_prime(['13','37','61','307','353','601']) => 6
        count_prime(['13','37','61','307','353','601','88','909']) => 6
        '''
        count = 0
        if latex == []:
                return count
        
        for num in latex:
                try:
                        if int(num) > 2 and not(has_a_factor(int(num),int(num)-1)):
                            count += 1
                except ValueError:
                        pass
        return count

## Testing Examples:
check.expect("EX1", count_prime(['1','4','10','17','71','97']),3)
check.expect("EX2", count_prime([]),0)
check.expect("EX3", count_prime(['2','4','6','8']),0)
check.expect("EX4", count_prime(['1']),0)
check.expect("EX5", count_prime(['13','37','61','307','353','601']),6)
check.expect("EX6", count_prime(['13','37','61','307','353','601','88','909']),6)
    
    

    