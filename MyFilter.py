def even(x):
    """"The function determines if the input is even or not."""
    if x%2 == 0:
        return True
    else:
        return False

def myFilter(func, List):
    """"The function filters out even numbers and prints them in a new list"""
    if List:
        if func(List[0]) is True:
            return [List[0]] + myFilter(func, List[1:])
        else:
            return myFilter(func, List[1:])
    else:
        return []
    if True:
       return (List)
