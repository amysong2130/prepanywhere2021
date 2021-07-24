#function to DETECT the number of limits and print number of occurences

#code for regex in python - using strings not tables
import re
file = open('limits.csv')

text = file.read()

pattern = '\\\lim(its)?(\\\limits)?\_\{'

#to print number of occurences
print('Number of occurences of limits:\n', len(re.findall(pattern,text)))

#to print all matches
print('Here are all of the matches of limits:\n')
for match in re.finditer(pattern,text):
    print(match)

file.close()

##regex pattern
#\\lim(its)?(\\limits)?\_\{


##tests for regex
#\lim_{
#\limits_{
#\lim\limits_{

#lim
#limits
#lim\limits
#\lim
#\limits
