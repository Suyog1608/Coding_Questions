def swap_two_no(list1):
    a = list1[0]
    list1[0] = list1[-1]
    list1[-1] = a
    print("list after swapping th numbers", list1)

    '''another method'''
    # list1[0], list1[-1] = list1[-1], list1[0]

    # start, *middle, end = list1
    # list1 = [end, *middle, start]
    #
    # print("list after swapping th numbers", list1)


list1 = []
for i in range(0, 5):
    num = int(input("enter the number: "))
    list1.append(num)
print(list1)
swap_two_no(list1)
