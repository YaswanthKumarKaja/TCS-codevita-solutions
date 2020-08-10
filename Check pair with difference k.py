'''Given an array A of sorted integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

Input Format
First line is number of test cases T. Following T lines contain:
N, followed by N integers of the array
The non-negative integer k
Output format
Print 1 if such a pair exists and 0 if it doesn’t.

Example
Input
1
3 1 3 5
4

Output:
1

'''
def fune(a,diff):
    left = 0
    right = 1
    while (left <= right):
        if a[right] - a[left] == diff:
            return 1
        elif a[right]-a[left]<diff:
            if right!=len(a)-1:
                right+=1
            else:
                return 0
        elif a[right]-a[left]>diff:
            if left!=len(a)-1:
                left+=1
            else:
                return 0
    return 0



T=int(input())
for _ in range(T):
    a=list(map(int,input().split()))
    diff=int(input())
    if fune(a,diff)==1:
        print("1")
    else:
        print("0")
'''def isdiffk(a,k):
    l=0
    h=0
    a.sort()
    #print(a)
    while h<=len(a)-1 or l<=len(a)-1:
        #print(l,h,a[h]-a[l])
        if a[h]-a[l]==k:
            return 1
        elif a[h]-a[l]<k:
            if h!=len(a)-1:
                h+=1
            else:
                return 0
        elif a[h]-a[l]>k:
            if l!=len(a)-1:
                l+=1
            else:
                return 0
    if h==len(a):
        return 0

T=int(input())
for T1 in range(T):
    a=list(map(int,input().split()))
    n=a[0]
    del a[0]
    k=int(input())
    if isdiffk(a,k) ==1:
        print(1)
    else:
        print(0)'''




