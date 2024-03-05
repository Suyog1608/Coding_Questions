def swapAnyTwoNo(list1, pos1, pos2):
    list1[pos1], list1[pos2] = list1[pos2], list1[pos1]
    print("after swapping", list1)


list1 = [2, 4, 6, 8, 9, 10]
pos1 = int(input("enter the position in b/w the length of list (0-5): "))
pos2 = int(input("enter the position to replace in b/w len of list (0-5): "))
print(list1)
swapAnyTwoNo(list1, pos1, pos2)
