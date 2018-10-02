fhandle = open ("romeo.txt")
wordslist = list()
for lines in fhandle :
    line = lines.rstrip()
    words = line.split()
    for items in words:
        if items not in wordslist :
            wordslist.append(items)
        else :
            continue
wordslist.sort()
print (wordslist)
