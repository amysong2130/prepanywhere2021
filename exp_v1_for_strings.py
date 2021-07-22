#function to detect the number of exponential functions (e^x)

#code for regex in python - using strings not tables
import re

text = 'e^{x+5},e,e^8,\exp(4+y),\exp(y),exp'

pattern = '\\\?e(xp)?\^?[\(\{]?(\w)+'

#to print number of occurences
print('occurence of exp:', len(re.findall(pattern,text))) 

#to print all matches
for match in re.finditer(pattern,text):
    print(match)

##regex pattern
#\\?e(xp)?\^?[\(\{]?(\w)+


##tests for regex
#e^{x+5}
#e^{3}
#\exp(y)
#\exp(4)
#\exp(4+y)
#e^x
#e^8