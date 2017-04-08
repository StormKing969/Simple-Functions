def explode(s):
    if s:
        list0 = [s[0]] + explode(s[1:])
        return list0
    else:
        list1=[]
        return list1
