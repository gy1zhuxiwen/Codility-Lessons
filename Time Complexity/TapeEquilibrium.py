#��һ���ϴ�
#def solution(A):
#    lsum = 0
#    rsum = sum(A)
#    minimal = abs(lsum-rsum)
#    for i in A:
#        lsum += i
#        rsum -= i
#        minimal = min(minimal,abs(lsum-rsum))
#    return minimal
#����ԭ��i��λ��Ӧ�ñ�len(A)С1�Ŷԣ�������ٱ���һ��Ԫ��
#
#�ڶ����ϴ�
#def solution(A):
#    lsum = 0
#    rsum = sum(A)
#    minimal = abs(lsum-rsum)
#    for i in range(1,len(A)-1):
#        lsum += A[i]
#        rsum -= A[i]
#        minimal = min(minimal,abs(lsum-rsum))
#    return minimal
#����ԭ��minimal���ܳ�ʼ��Ϊabs(sum(A))����Ϊ��ֵ���ܱȺ���������������ֵ����С

#�������ϴ� 100% 100%
def solution(A):
    lsum = A[0]
    rsum = sum(A)-A[0]
    minimal = abs(lsum-rsum)
    for i in range(1,len(A)-1):
        lsum += A[i]
        rsum -= A[i]
        minimal = min(minimal,abs(lsum-rsum))
    return minimal