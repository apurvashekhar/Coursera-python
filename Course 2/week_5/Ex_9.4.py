#open file
name = input("Enter file:")
handle = open(name)
counts = dict()
#look for lines starting with 'From' and take [1] word
for line in handle:
    if not line.startswith('From ') :
        continue
    lines = line.split()
    lines = lines [1]
    counts[lines] = counts.get (lines, 0) + 1
print (counts)
bigword = None
bigcount = None
for word,count in counts.items ():
    if bigcount is None or count > bigcount :
        bigword= word
        bigcount= count
print (bigword, bigcount)
