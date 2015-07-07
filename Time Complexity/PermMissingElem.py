#first time submit C20% P80%
#def solution(A):
#    return (set(range(1,len(A)+1)) - set(A)).pop()
#error£ºThe length of the range calculated error.

#second time submit C100% P100%
def solution(A):
    return (set(range(1,len(A)+2)) - set(A)).pop()