hours = input("Enter hours: ")
rate = input("Enter rate: ")
try:
    ihours = float(hours)
    irate = float(rate)
    if ihours < 40 :
        pay = ihours * irate
        print (pay)
    elif ihours > 40 :
        pay = (40 * irate) + (ihours - 40) * (1.5 * irate)
        print (pay)
except:
    print ("Error, please enter numeric input")
