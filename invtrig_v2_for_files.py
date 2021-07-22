#function to detect the number of inverse trig functions

#code for regex in python - using strings not tables
import re
file = open('trig inverse data.csv')

text = file.read()

pattern = '(([Aa]rc(sine?|cos|tan|csc|sec|cot))|(([Ss]ine?|[Cc]os|[Tt]an|[Cc]sc|[Ss]ec|[Cc]ot)inv)|(\{?([Ss]ine?|[Cc]os|[Tt]an|[Cc]sc|[Ss]ec|[Cc]ot)\}?\^\{-1\}))'

#to print number of occurences
print('occurence of arc_trig:', len(re.findall(pattern,text))) 

#to print all matches
for match in re.finditer(pattern,text):
    print(match)
    
file.close()

##regex pattern
#(([Aa]rc(sine?|cos|tan|csc|sec|cot))|
#(([Ss]ine?|[Cc]os|[Tt]an|[Cc]sc|[Ss]ec|[Cc]ot)inv)|
#(\{?([Ss]ine?|[Cc]os|[Tt]an|[Cc]sc|[Ss]ec|[Cc]ot)\}?\^\{-1\}))

##tests for regex
#arcsin
#arccscx
#Arctan
#Arccotx
#sininv
#Cosinv
#{Csc}^{-1}
#{sin}^{-1}