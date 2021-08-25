#function to DETECT the number of div tags and print number of occurences

#code for regex in python - using strings not tables
import re
file = open('html-example.html')

text = file.read()

pattern = '<div'

#to print number of occurences
print('Number of occurences of div tags:\n', len(re.findall(pattern,text)))

#to print all matches
print('Here are all of the matches of div tags:\n')
for match in re.finditer(pattern,text):
    print(match)

file.close()

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