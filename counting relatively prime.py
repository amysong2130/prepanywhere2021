import check
import math

def is_relativelyprime(latex):
        '''
        Parameters
        ----------
        latex: list of str
           each element should be a natural number in format of string
        
        Returns
        -------
           returns pandas Series with True if the numbers are relatively 
           prime, otherwise returns False
           
        <relatively prime: if integers share no common positive 
                           factors except 1>
                           
        Requires
        --------
           the list must have at least two elements
           
        Examples
        --------
        is_relativelyprime(['1','4','10','17','71','97']) => False
        is_relativelyprime([]) => False
        is_relativelyprime(['99']) => False
        is_relativelyprime(['2','3','4','5']) => False
        is_relativelyprime(['2','3','7']) => True
        is_relativelyprime(['8','3','7']) => True
        is_relativelyprime(['18','3','7']) => False
        
        '''
        if len(latex) < 2:
                return False
        else:
                i = 0
                while i < len(latex):
                        a = int(latex[i])
                        j = i + 1
                        while j < len(latex):
                                b = int(latex[j])
                                pair = [a, b]
                                if math.gcd(*pair) != 1:
                                        return False
                                j += 1
                        i += 1
        return True

## Testing Examples:
check.expect("EX1", is_relativelyprime(['1','4','10','17','71','97']),False)
check.expect("EX2", is_relativelyprime([]),False)
check.expect("EX3", is_relativelyprime(['99']),False)
check.expect("EX4", is_relativelyprime(['2','3','4','5']),False)
check.expect("EX6", is_relativelyprime(['8','3','7']),True)
check.expect("EX7", is_relativelyprime(['18','3','7']),False)