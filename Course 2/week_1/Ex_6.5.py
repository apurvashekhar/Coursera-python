data = 'X-DSPAM-Confidence:0.8475'
colon = data.find(':')
parsed = float(data[colon + 1 : len(data)])
print (parsed)
