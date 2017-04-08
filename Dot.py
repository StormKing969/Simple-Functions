def dot(list1, list2):
    if list1 and list2:
        return list1[0] * list2[0] + dot(list1[1:], list2[1:])
    else:
        return 0 
