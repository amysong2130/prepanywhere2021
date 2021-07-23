#function to DETECT the number of pi then REMOVE the pi

#code for regex in python - using strings not tables
import re

file = open('pi with trig.csv')

text = file.read()

pattern = '\\b(up)?[Pp][Ii]\\b'

#to print number of occurences
print('Number of occurences of pi:\n', len(re.findall(pattern,text)))

#to print all matches
print('Here are all of the matches of pi:\n')
for match in re.finditer(pattern,text):
    print(match)
    
#to remove all matches and print new list
new_list = re.sub(pattern,'',text)
print('This is the document now without any pi:\n', new_list)

file.close()

##regex pattern
#\b(up)?[Pp][Ii]\b


##tests for regex
#pi
#PI
#Pi
#uppi
#pie
#(pi)
#pizza
#pi^2
#mississipi