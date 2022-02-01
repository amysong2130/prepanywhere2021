import check

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
                        if int(num) >= 2:
                            factors = 2
                            for i in range(2,int(num)):
                                if not (int(num) % i):
                                    factors += 1
                            if factors == 2: 
                                count += 1
                except ValueError:
                        pass
        return count

## Testing Examples:
check.expect("EX1", count_prime(['1','4','10','17','71','97']),3)
check.expect("EX2", count_prime([]),0)
check.expect("EX3", count_prime(['2','4','6','8']),1)
check.expect("EX4", count_prime(['1']),0)
check.expect("EX5", count_prime(['13','37','61','307','353','601']),6)
check.expect("EX6", count_prime(['13','37','61','307','353','601','88','909']),6)
check.expect("EX7", count_prime(['131','3700','6134','3072','353345','60123','88','909352']),1)
    
    

    