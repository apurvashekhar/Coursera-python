#Add code to the above program to figure out who has the
#most messages in the file. After all the data has been read and the dictionary
#has been created, look through the dictionary using a maximum
#loop (see Chapter 5: Maximum and minimum loops) to find who has
#the most messages and print how many messages the person has.
#Enter a file name: mbox-short.txt
#cwen@iupui.edu 5
#Enter a file name: mbox.txt
#zqian@umich.edu 195


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
