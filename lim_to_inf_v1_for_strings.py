#function to DETECT the number of limits to +/- infinity and print number of occurences

#code for regex in python - using strings not tables
import re

text = '$\lim_{x \to +\infty} f(x)$,$\lim_{x \to -\infty} f(x)$,$\lim_{n\to\infty}$'

pattern = '\\\lim\_\{[a-z]( )?\\\to( )?[+-]?\\\infty\\}'

#to print number of occurences
print('Number of occurences of limits to infinity:\n', len(re.findall(pattern,text)))

#to print all matches
print('Here are all of the matches of limits to infinity:\n')
for match in re.finditer(pattern,text):
    print(match)

##regex pattern
#\\lim\_\{[a-z]( )?\\to( )?[+-]?\\infty\}


##tests for regex
#$\lim_{x \to +\infty} f(x)$
#$\lim_{x \to -\infty} f(x)$
#$\lim_{n\to\infty}$