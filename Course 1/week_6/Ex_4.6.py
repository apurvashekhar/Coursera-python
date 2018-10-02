def computepay(h,r):
    if h >= 40 :
        pay = ((r*0.5)*(h-40)) + (h*r)
        print (pay)
        return pay
    elif h < 40 :
        pay = h * r
        print (pay)
        return pay
    else:
        print ('Please enter numeric input')
hrs = input('Enter Hours:')
h = float(hrs)
rte = input ('Enter Rate:')
r = float(rte)
computepay (h,r)
