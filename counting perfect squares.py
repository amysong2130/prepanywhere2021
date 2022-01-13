import re
import math
import check
    
def count_psquares(latex):
        '''
        Parameters
        ----------
        latex: list of str
           each element should be a natural number in format of string
        
        Returns
        -------
           returns pandas Series with count of perfect squares
           
        Examples
        --------
        count_psquares(['1','4','10','17','71','97']) => 2
        count_psquares([]) => 0
        count_psquares(['1']) => 1
        count_psquares(['5']) => 0
        count_psquares(['81','10000','144']) => 3
  
        '''
        count = 0
        if latex == []:
                return count
        
        for num in latex:
                sqrt = math.sqrt(int(num))
                result = re.match("[+]?\d+\.?0?$", str(sqrt))
                try:
                        if result is not None:
                                count += 1
                except ValueError:
                        pass
        return count

## Testing Examples:
check.expect("EX1", count_psquares(['1','4','10','17','71','97']),2)
check.expect("EX2", count_psquares([]),0)
check.expect("EX3", count_psquares(['1']),1)
check.expect("EX4", count_psquares(['5']),0)
check.expect("EX5", count_psquares(['81','10000','144']),3)