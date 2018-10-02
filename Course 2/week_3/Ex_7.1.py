# Use words.txt as the file name
fname = input("Enter file name: ")
fhandle = open(fname)
for lines in fhandle:
    result = lines.rstrip()
    print(result.upper())
