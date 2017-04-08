def removeAll(element,List):
    """"This function takes in two arguments and prints out a new list without the element"""
    if List:
        if List[0] == element:
            List1 = removeAll(element, List[1:])
            return List1
        else:
            List1 = [List[0]]+removeAll(element,List[1:])
            return List1
    else:
        return List
