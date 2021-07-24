#function to detect the number of exponential functions (e^x)

#code for regex in python - using strings not tables
import re
file = open('e.csv')

text = file.read()

pattern = '\\\?e((xp)|\^)[\(\{]?(\w)+'

#to print number of occurences
print('occurence of exp:', len(re.findall(pattern,text))) 

#to print all matches
for match in re.finditer(pattern,text):
    print(match)
    
file.close()

##regex pattern
#\\?e((xp)|\^)[\(\{]?(\w)+


##tests for regex
#e^{x+5}
#e^{3}
#\exp(y)
#\exp(4)
#\exp(4+y)
#e^x
#e^8