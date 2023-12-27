import sys
import re
print (sys.argv[1:])

pattern = r"^--([^=]+)(=(.+)|)$"

a = "--model=layers"
b = "--model/layers=3"
c = "--model-layers=7"
d = "--yes"
e = "sd--aa=layers"
f = "sd--yes"

for x in [a,b,c,d,e,f,]:
    match = re.match(pattern, x)
    if match is not None:
        print (match.group(1), match.group(3))
    else:
        print ("None")