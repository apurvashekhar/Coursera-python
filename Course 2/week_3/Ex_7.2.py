# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fhandle = open(fname)
count = 0
total = 0
for line in fhandle:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    line = line.replace("X-DSPAM-Confidence:","")
    line = line.strip()
    total = total + float(line)
    count = count + 1
    average = total/count
print (average)
