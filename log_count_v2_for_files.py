#function to detect the number of logarithmic functions

#code for regex in python - using strings not tables
import re
file = open('log expressions.csv')

text = file.read()

pattern = '\\\[Ll]o?[gn][\s\S]'

#to print number of occurences
print('occurence of log:', len(re.findall(pattern,text))) 

#to print all matches
for match in re.finditer(pattern,text):
    print(match)
    
file.close()

##regex pattern
#\\[Ll]o?[gn][\s\S]+


##tests for regex
#\log 
#\lg 
#\ln 
#\Log 
#\log 
#\Ln 
#\log3 
#\log_10 4
#\log_a b
#\log_{5} 4
#\log_888
#\log_{2} (2x+5)
#\log_{3}(-2x-6)
#\log_{x} (y)
#\log_{3x}
