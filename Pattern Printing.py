'''Decode the logic and print the Pattern that corresponds to given input.

If N= 3

then pattern will be :

10203010011012
**4050809
****607
If N= 4, then pattern will be:

1020304017018019020
**50607014015016
****809012013
******10011
Constraints
2 <= N <= 100
Input Format
First line contains T, the number of test cases
Each test case contains a single integer N
Output
First line print Case #i where i is the test case number
In the subsequent line, print the pattern
Test Case 1
3
3
4
5
Output
Case #1
10203010011012
**4050809
****607
Case #2
1020304017018019020
**50607014015016
****809012013
******10011
Case #3
102030405026027028029030
**6070809022023024025
****10011012019020021
******13014017018
********15016
'''

t=int(input())
for t1 in range(t):
    n=int(input())
    inc=1
    print("Case #",t1+1,sep="")
    for i in range(n):
        print(i*"**",end="")
        dec=((n-i)**2)+inc
        for j in range(n-i):
            print(inc,"0",sep="",end="")
            inc+=1
        for j in range(n-i):
            if j==n-i-1:
                print(dec,end="")
            else:
                print(dec,"0",sep="",end="")
                dec+=1
        print()
        