#This program counts the distribution of the hour of the day
#for each of the messages. You can pull the hour from the “From” line
#by finding the time string and then splitting that string into parts using
#the colon character. Once you have accumulated the counts for each
#hour, print out the counts, one per line, sorted by hour as shown below.
#python timeofday.py
#Enter a file name: mbox-short.txt
#04 3
#06 1
#07 1
#09 2
#10 3
#11 6
#14 1
#15 2
#16 4
#17 2
#18 1
#19 1
name = input("Enter file:")
handle = open(name)
counts = dict()
#look for lines starting with 'From' and take [5] word
for line in handle:
    if not line.startswith('From ') :
        continue
    lines = line.split()
    hours = lines [5]
    hour = hours.split (':')
    newhour = hour [0]
    counts[newhour] = counts.get (newhour, 0) + 1

lst = list ()

for key,value in counts.items ():
    lst.append ( (key,value))
lst.sort()

for h, counts in lst:
    print (h, counts)
