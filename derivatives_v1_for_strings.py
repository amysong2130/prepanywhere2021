#function to DETECT the number of derivatives and print number of occurences
## note: this code has only been tested with test cases, not a dataset

#code for regex in python - using strings not tables
import re

text = "frac{1}{2},\frac{b}{c+d},\dfrac{b}{c+d},\frac{\frac{1}{x}}{\sin{x}\cdot x^2},\frac{P(x)}{Q(x)},\frac{\partial u}{\partial t},\frac{\partial^2 u}{\partial x^2},$f'(x)$,$f''(x)$,$f^{(k)}(x)$,\dfrac{dy},\frac{dy},\dfrac{\mathrm{d}y},\frac{\mathrm{d}y},\frac{d},\frac{du},\frac{d^2 u},\frac{d^3 y},\tfrac{dy},\frac{df},y',y'',(x^2+5x+3)'"

pattern = 'frac{(?!\d)d\w?|frac{\\\mathrm\{d}\w}|\$f\'\'?\(\S|\$f\^{\(\S|y\'|\(\S+\)\''

#to print number of occurences
print('Number of occurences of derivatives:\n', len(re.findall(pattern,text)))

#to print all matches
print('Here are all of the matches of derivatives:\n')
for match in re.finditer(pattern,text):
    print(match)

##regex pattern
#frac{(?!\d)d\w?|frac{\\mathrm\{d}\w}|\$f\'\'?\(\S|\$f\^{\(\S|y\'|\(\S+\)\'

##tests for regex
##should match all derivatives EXLUDING partial derivatives
#$f'(x)$
#$f''(x)$
#$f^{(k)}(x)$
#\dfrac{dy}{dx}
#\frac{dy}{dx} 
#\dfrac{\mathrm{d}y}{\mathrm{d}x} 
#\frac{\mathrm{d}y}{\mathrm{d}x} 
#\frac{d}{dx}
#\frac{du}{dt}
#\frac{d^2 u}{dx^2}
#\frac{d^3 y}{dx^3}
#\tfrac{dy}{dx}
#\frac{df}{dx} 
#y'
#y''
#(x^2+5x+3)'

##should not match
#\frac{1}{2}
#\frac{b}{c+d}
#\dfrac{b}{c+d}
#\frac{\frac{1}{x}}{\sin{x}\cdot x^2}
#\frac{P(x)}{Q(x)}
#\frac{\partial u}{\partial t}
#\frac{\partial^2 u}{\partial x^2}