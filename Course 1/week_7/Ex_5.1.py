largest = None
smallest = None
while True:
    data = input('Enter a number: ')
    if data == 'done':
        break
    try:
        num = int(data)
        lst= list()
        lst.append(num)
    except:
        print ('Invalid input')
    else:
        for numbers in lst:
            if smallest is None:
               smallest = num
               largest = num
            elif num < smallest:
               smallest = num
           elif num > largest:
               largest = num
print(lst)
print(smallest, num, largest)
