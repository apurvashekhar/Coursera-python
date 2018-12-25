#In this assignment you will read through and parse a file with text and numbers.
#You will extractall the numbers in the file and compute the sum of the numbers.

import re
fname = input ('Enter file name: ')
fhandle = open(fname)
lst = list()
total = 0
#To extract all the numbers
for lines in fhandle:
    line = lines.rstrip()
    newline = re.findall('[0-9]+',line)
    #to convert all the list into single list.
    for numbers in newline:
        if numbers in lst:
            continue
        else:
            total = total +int(numbers)
print (total)
