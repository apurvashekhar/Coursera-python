hours = input("Enter hours: ")
rate = input("Enter rate: ")
if float(hours) < 40 :
    pay = float(hours) * float (rate)
    print (pay)
elif float(hours) > 40 :
   pay = (40 * float (rate)) + (float (hours) - 40) * (1.5 *float (rate))
   print (pay)
