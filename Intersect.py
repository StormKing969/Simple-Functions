def intersect(s1, s2):
    """This function takes input as two lists and whatever elements
    common are printed out in a seperate list"""
    if not s1 or not s2:
        s3=[]
        return s3
    elif s2[0] in s1:
        return [s2[0]]+ intersect(s1, s2[1:])
    else:
        return intersect(s1,s2[1:])
