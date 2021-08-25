#function to DETECT the number of decimals and print number of occurences

#code for regex in python - using strings not tables
import re
file = open('trig inverse data.csv')

text = file.read()

pattern = '(\d\.\d|\d\.\\\overline{)'

#to print number of occurences
print('Number of occurences of decimals:\n', len(re.findall(pattern,text)))

#to print all matches
print('Here are all of the matches of decimals:\n')
for match in re.finditer(pattern,text):
    print(match)

file.close()

##regex pattern
#(\d\.\d|\d\.\\\overline{)

##tests for regex
#123.0
#0.5
#0.3333
#-0.25
#13.95
#678,234.35
#$35.99
#-8999.9
#0.\overline{142857}
#x^{1.09}
#5^{2.5}

#12334
#567,876,234
#end sentence with 33.