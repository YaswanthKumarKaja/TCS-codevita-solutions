'''
Our Own Chessboard
Let’s print a chessboard!

Write a program that takes input:

The first line contains T, the number of test cases
Each test case contains an integer N and also the starting character of the chessboard
Output Format
Print the chessboard as per the given examples

Sample Input / Output
Input:
2
2 W
3 B

Output:
WB
BW
BWB
WBW
BWB
'''

def myfun(a,b,n):
    for i in range(n):
        for j in range(n):
            if (i+j)%2==0:
                print(a,end="")
            else:
                print(b,end="")
        print("")
T=int(input())
for T1 in range(T):
    n,p=input().split()
    n=int(n)
    if p=="B":
        myfun("B","W",n)
    else:
        myfun("W","B",n)