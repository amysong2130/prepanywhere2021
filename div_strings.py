#function to DETECT the number of 'div' and print number of occurences

#code for regex in python - using strings not tables
import re

text = '<div>,</div>,<div class,<div style,<div id,divide,division,divergence'

pattern = '<div'

#to print number of occurences
print('Number of occurences of div:\n', len(re.findall(pattern,text)))

#to print all matches
print('Here are all of the matches of div:\n')
for match in re.finditer(pattern,text):
    print(match)

##regex pattern
#<div

##tests for regex
#<div> 
#</div>
#<div class
#<div style
#<div id
#divide
#division
#divergence
