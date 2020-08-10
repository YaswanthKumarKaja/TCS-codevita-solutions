'''Longest Progressive Sequence
Given a sequence, the objective is to find the longest progressive sequence arranged in ascending order. Detailed descriptions are as:

A sequence is said to be progressive if it doesn’t decrease at any point in time.
For example 1 1 2 2 is a progressive sequence but 1 2 1 is not a progressive sequence. Let S be the sequence and be represented by T spaced integers Ki, now your task is to find out the first longest progressive sequence present in the given sequence (S).

Input Format:
First line will contain N, the number of test cases. After than 2*N lines follow.

For each test case, the first line will contain T, the length of the sequence and next line will contain T spaced integers Ki (where i = 0,1, ...,L).

Line 1 T,where T is the length of the sequence
Line 2 Ki,where Ki is integer in sequence separated by space
Constraints:
1<=T<=10^6 (one million)
-10^9<=Ki<=10^9 (one billion)
Output Format:
Line 1 longest progressive sequence present in the given sequence
If more than 1 sequence exists, then print the one whose starting index is least, i.e., the one that comes first.

Sample Test Cases:
Input:

1
4
1 1 2 1
Output:

1 1 2
Input:

1
5
1 2 1 2 2
Output:

1 2 2
'''
T=int(input())
for T1 in range(T):
    n=int(input())
    a=list(map(int,input().split()))
    stop=0
    start=0
    count=1
    maxstop=0
    maxstart=0
    maxcount=0
    for i in range(1,n):
        if a[i]>=a[i-1]:
            stop=i
            count+=1
        else:
            if maxcount<count:
                maxcount=count
                maxstart=start
                maxstop=stop
            start=i
            stop=i
            count=1
    if maxcount < count:
        maxcount = count
        maxstart = start
        maxstop = stop
    for i in range(maxstart,maxstop+1):
        print(a[i],end=" ")
    print("")