#Download a copy of the file www.py4e.com/code3/romeo.txt.
#Write a program to open the file romeo.txt and read it line by line. For
#each line, split the line into a list of words using the split function.
#For each word, check to see if the word is already in a list. If the word
#is not in the list, add it to the list. When the program completes, sort
#and print the resulting words in alphabetical order.
#Enter file: romeo.txt
#['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
#'and', 'breaks', 'east', 'envious', 'fair', 'grief',
#'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
#'sun', 'the', 'through', 'what', 'window',
#'with', 'yonder']


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
