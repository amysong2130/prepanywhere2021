import check

def common_diff(latex):
        '''
        Parameters
        ----------
        latex: list of str
           each element should be a natural number in format of string
        
        Returns
        -------
           returns 1 if there is a common difference between integers (abs val)
           returns 0 otherwise
           
        Examples
        --------
        common_diff(['1']) => 0
        common_diff([]) => 0
        common_diff(['2','4','6','8']) => 1
        common_diff(['3','6','9']) => 1
        common_diff(['13','26','39','52','65']) => 1
        common_diff(['13','37','61','307','353','601','88','909']) => 0
        '''
        if len(latex) < 2:
                return 0
        first = int(latex[0])
        second = int(latex[1])
        diff = abs(second - first)
        i = 2
        while i < len(latex):
                try:
                        if abs(int(latex[i]) - int(latex[i-1])) != diff:
                                return 0
                        i += 1  
                except ValueError:
                        pass
        return 1

## Testing Examples:
check.expect("EX1", common_diff(['1']), 0)
check.expect("EX2", common_diff([]), 0)
check.expect("EX3", common_diff(['3','6','9']), 1)
check.expect("EX4", common_diff(['13','26','39','52','65']), 1)
check.expect("EX5", common_diff(['13','37','61','307','353','601','88','909']), 0)
check.expect("EX6", common_diff(['1','4','7','10']), 1)
check.expect("EX7", common_diff(['1','-2','1','-2']), 1)

    
    

