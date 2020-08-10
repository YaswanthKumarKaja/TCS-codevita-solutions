'''Count the Factor
The factorial of a non-negative integer N, denoted by N!, is the product of all positive integers less than and equal to N.
Factorial of any number can be represented in simplest form of its prime factors.
e.g. 4!=4*3*2*1= 2^3 * 3^1 (where ^ means exponent)

Factorials can also be specified by the number of times each prime factors occurs in it, thus 24 could be specified as (3 1) meaning 3 twos, 1 three.

Write a program that will take an integer as input and give output as the following.

Input Format
Input will be a positive integer N where N>1.
Line 1: N,where N is any integer.

Output Format
Output will show a series consists of the number of times each prime factor appears after the factorization of N! separated by spaces.

For Valid Input, print

L, where L is the series consists of the number of times each prime factor appears after the factorization of N! separated by spaces.

For Invalid Input,print

Invalid Input

Sample Test Cases
Input
6

Output
4 2 1

Input
a

Output
Invalid Input

Input
-5

Output
Invalid Input

'''

def isprime(n):
    if n==2 or n==3 or n==5:
        return 1              # Function to find prime or not
    elif n%2==0 or n%3==0 or n%5==0:
        return 0
    elif n%6==5 or n%6==1:
        r=int(n**0.5)
        for i in range(2,r+1):
            if n%i==0:
                return 0
            elif i==r:
                return 1
    else:
        return 0
n=int(input())
pl=[]
for i in range(2,int(n)+1):
    if isprime(i)==1:
        pl.append(i)
#print(pl)
di={}
for i in range(2,n+1):
    temp=i
    j=0
    while(temp>1):
        if temp%pl[j]==0:
            temp//=pl[j]
            if pl[j] in di:
                di[pl[j]]+=1
            else:
                di[pl[j]]=1
        else:
            j+=1
#print(di)
for i,j in di.items():
    print(j,end=" ")