#第一次上传
#def solution(A):
#    lsum = 0
#    rsum = sum(A)
#    minimal = abs(lsum-rsum)
#    for i in A:
#        lsum += i
#        rsum -= i
#        minimal = min(minimal,abs(lsum-rsum))
#    return minimal
#错误原因：i的位置应该比len(A)小1才对，后段至少保留一个元素
#
#第二次上传
#def solution(A):
#    lsum = 0
#    rsum = sum(A)
#    minimal = abs(lsum-rsum)
#    for i in range(1,len(A)-1):
#        lsum += A[i]
#        rsum -= A[i]
#        minimal = min(minimal,abs(lsum-rsum))
#    return minimal
#错误原因：minimal不能初始化为abs(sum(A))，因为该值可能比后面迭代计算出来的值都更小

#第三次上传 100% 100%
def solution(A):
    lsum = A[0]
    rsum = sum(A)-A[0]
    minimal = abs(lsum-rsum)
    for i in range(1,len(A)-1):
        lsum += A[i]
        rsum -= A[i]
        minimal = min(minimal,abs(lsum-rsum))
    return minimal