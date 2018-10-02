fname = input("Enter file name: ")
fhandle = open(fname)
count = 0
for line in fhandle:
    if not line.startswith('From '):
        continue
    count = count + 1
    message = line.strip()
    if not message.startswith('From '):
        continue
    idname = message.split()
    print (idname[1])
    continue
print ("There were", count , "lines in the file with From as the first word")
