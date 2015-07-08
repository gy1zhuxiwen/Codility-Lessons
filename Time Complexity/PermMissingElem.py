#First time submit C20% P80%
def solution(A):
    return (set(range(1,len(A)+1)) - set(A)).pop()
#Error£ºThe length of the range calculated error.

#Second time submit C100% P100%
def solution(A):
    return (set(range(1,len(A)+2)) - set(A)).pop()
    
#Third time submit C100% P100%
#Another solution, but the "sum" method cost more time than the "set"
def solution(A):
    N = len(A)
    total = (N+1)*(N+2)/2
    return total - sum(A)