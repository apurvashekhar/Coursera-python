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
