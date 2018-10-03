directory = dict()
while True:
    question = input("Do you want to co")
    if question == "yes" :
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        number = input("Enter number: ")
        directory[(first_name, last_name)] = int(number)
    else : break


#Directory
directoryquestion = input("Do you want to print directory? ")
if directoryquestion == "yes" :
    for (first_name, last_name) in directory.keys():
        print(first_name, last_name, directory[(first_name, last_name)])

searchquestion = input("Do you want to search a contact? ") #search by name
if searchquestion == "yes" :
    first = input("Enter first name :")
    last = input("Enter last name: ")
    if (first, last) in directory.keys():
        print(directory[(first_name, last_name)])
    if (first, last) not in directory.keys() :
        print("No entry found")
