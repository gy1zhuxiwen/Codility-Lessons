#First time submit C66% P100%
def solution(A):
    lsum = 0
    rsum = sum(A)
    minimal = abs(lsum-rsum)
    for i in A:
        lsum += i
        rsum -= i
        minimal = min(minimal,abs(lsum-rsum))
    return minimal
#Error��The position of ��i�� should equal len(A)-1, for that the bottom half is not empty.

#Second time submit C16% P33%
def solution(A):
    lsum = 0
    rsum = sum(A)
    minimal = abs(lsum-rsum)
    for i in range(1,len(A)-1):
        lsum += A[i]
        rsum -= A[i]
        minimal = min(minimal,abs(lsum-rsum))
    return minimal
#Error��The value of 'minimal' should not initial with abs(sum(A)),this value maybe less than the value calculate next.

#Third time submit C100% P100%
def solution(A):
    lsum = A[0]
    rsum = sum(A)-A[0]
    minimal = abs(lsum-rsum)
    for i in range(1,len(A)-1):
        lsum += A[i]
        rsum -= A[i]
        minimal = min(minimal,abs(lsum-rsum))
    return minimal