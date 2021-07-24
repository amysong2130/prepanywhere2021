#function to DETECT the number of limits and print number of occurences

#code for regex in python - using strings not tables
import re
file = open('INSERT_NAME.csv')

text = file.read()

pattern = '\\\lim\_\{[a-z]( )?\\\to( )?[+-]?\\\infty\\}'

#to print number of occurences
print('Number of occurences of limits:\n', len(re.findall(pattern,text)))

#to print all matches
print('Here are all of the matches of limits:\n')
for match in re.finditer(pattern,text):
    print(match)

file.close()

##regex pattern
#\\lim\_\{[a-z]( )?\\to( )?[+-]?\\infty\}


##tests for regex
#$\lim_{x \to +\infty} f(x)$
#$\lim_{x \to -\infty} f(x)$
#$\lim_{n\to\infty}$