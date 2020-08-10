'''Intersection of 2 Sorted Arrays
Find the intersection of two sorted arrays.
OR in other words,
Given 2 sorted arrays, find all the elements which occur in both the arrays.

Input Format
The first line contains T, the number of test cases. Following T lines contain:
Line 1 contains N1, followed by N1 integers of the first array
Line 2 contains N2, followed by N2 integers of the second array
Output Format
The intersection of the arrays in a single line

Example
Input:
1
3 10 17 57
6 2 7 10 15 57 246

Output:

10 57

Input:
1
6 1 2 3 3 4 5 6
2 1 6

Output:
1 6


'''
T = int(input())
for T1 in range(T):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    l1 = a[0]
    l2 = b[0]
    a = a[1:]
    b = b[1:]
    start1 = 0
    start2 = 0
    c = []
    while (start1 <= l1 - 1 and start2 <= l2 - 1):
        if a[start1] == b[start2]:
            c.append(a[start1])
            start2 += 1
            start1 += 1
        elif a[start1] < b[start2]:
            start1 += 1
        elif a[start1] > b[start2]:
            start2 += 1
    print(*c, end=" ")
    print("")

''''def final(a,b):
    #print(a,b)
    indae=0
    indbe=0
    c=[]
    while indae<=len(a)-1 and indbe<=len(b)-1:
        #print(indae,indbe)
        if a[indae]<=b[indbe]:
            if a[indae]==b[indbe]:
                c.append(a[indae])
            indae+=1
        elif b[indbe]<=a[indae]:
            if a[indae]==b[indbe]:
                c.append(a[indae])
            indbe+=1
    for i in c:
        print(i,end=" ")
    print("")



T=int(input())
for T1 in range(T):
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    an=a[0]
    bn=b[0]
    a.pop(0)
    b.pop(0)
    final(a,b)
'''
