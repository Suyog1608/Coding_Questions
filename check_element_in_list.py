def checkEleInList(list1, no):
    if no in list1:
        print("yes")
    else:
        print("no")


list1 = [10, 20, 30, 40]
no = int(input("enter the no. you want to search in list: "))
checkEleInList(list1, no)