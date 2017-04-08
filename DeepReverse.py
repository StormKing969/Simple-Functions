def deepReverse(List0):
    """The function takes in a list as an input and reverses it.
    Also reverses the fist inside of  a list."""
    if List0:
        if type (List0[0]) == type([1,2,3]):
            return deepReverse(List0[1:]) + [deepReverse(List0[0][1:])+[List0[0][0]]]
        else:
            return deepReverse(List0[1:]) + [List0[0]]
    else:
        return List0
