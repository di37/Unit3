#Loops on lists
##def print_all_elements(p):
##    i = 0
##    while i < len(p):
##        print (p[i])
##        i = i + 1
##
##print_all_elements([1,2,4])
##

##def print_all_elements(p):
##    for e in p:
##        print e
##print_all_elements([1,2,4])
##
##def sum_my_list(mylist):
##    total = 0
##    for s in mylist:
##        total = total + s
##    return total
##
##print(sum_my_list([1,2,3,10000000000000]))

##def measure_udacity(mylist):
##    i = 0
##    for name in mylist:
##        if (name[0] == 'U'):
##            i = i + 1
##    return i
##
##print(measure_udacity(['Udacity','Umbrella']))

##def find_element(mylist, value):
##    i = 0
##    for e in mylist:
##        if (e == value):
##            return i
##        i = i + 1
##    return -1
##
##print(find_element([1,2,3], 2))

# def find_element(mylist, value):
#    if value in mylist:
#        return mylist.index(value)
#    else:
#        return -1
# print(find_element([1,2,3], 3))

# def union(a,b):
#     for e in b:
#         if e not in p:
#             p.append(e)
