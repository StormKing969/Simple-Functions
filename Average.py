def average(L):
    if L:
        sumOfAll = L[0] + L[1] + average(L[2:])
        answer = sumOfAll/len(L)
        return answer
    else:
        return []
