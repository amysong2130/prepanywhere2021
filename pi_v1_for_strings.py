#function to DETECT the number of pi then REMOVE the pi

#code for regex in python - using strings not tables
import re

text = 'pi,PI,Pi,uppi,pie,(pi),pizza,pi^2,mississipi'

pattern = '\\b(up)?[Pp][Ii]\\b'

#to print number of occurences
print('occurence of pi:', len(re.findall(pattern,text)))

#to print all matches
for match in re.finditer(pattern,text):
    print(match)
    
#to remove all matches and print new list
new_list = re.sub(pattern,'',text)
print(new_list)

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
